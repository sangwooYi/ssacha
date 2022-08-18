from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import MovieSerializer, MovieTitleSerializer, CommentSerializer, ReviewSerializer, CommunitySerializer, GenreSerializer
from .models import Movie, Genre, Community, Review, Comment
from django.contrib.auth import get_user_model
from django.db.models import Q
import random

# Create your views here.

MBTI_DICT = {
# 장르 1개 / 키워드 2개 이렇게 MBTI별 요소 갯수를 통일
'ISTJ' : {
    'genre': '다큐멘터리', 
    'keyword': ['역사', '실화', '논리', '대중', '현실', '청렴', '결백', '솔로'],
    'positive_mbti': 'ENFP',
    'negative_mbti': 'ENFJ',
    },        
'ISFJ' : {
    'genre': '가족', 
    'keyword': ['권력', '자식', '아내', '전쟁', '과감', '자신감', '열정', '수호'],
    'positive_mbti': 'ENTP',
    'negative_mbti': 'ENTJ',
    },         
'INFJ' : {
    'genre': 'SF', 
    'keyword': ['공상', '심오', '이상', '예언', '종교', '선의', '단호', '결단'],
    'positive_mbti': 'ESTP',
    'negative_mbti': 'ESTJ',
    },        
'INTJ' : {
    'genre': '드라마', 
    'keyword': ['전술', '논쟁', '예술', '철학', '체스', '가십', '독서', '건축'],
    'positive_mbti': 'ESFP',
    'negative_mbti': 'ESFJ',
    },                
'ISTP' : {
    'genre': '모험', 
    'keyword': ['발명', '도구', '스파이', '본드', '선', '공정', '대접', '원리원칙'],
    'positive_mbti': 'ENFJ',
    'negative_mbti': 'ENFP',
    },        
'ISFP' : {
    'genre': '로맨스', 
    'keyword': [ '배려', '예술', '멜로', '공감', '재충전', '의미', '순수', '조화'],
    'positive_mbti': 'ENTJ',
    'negative_mbti': 'ENTP',
    },         
'INFP' : {
    'genre': '액션', 
    'keyword': ['꿈', '기괴', '기발', '영웅', '금', '뿌리', '자기표현', '해몽'],
    'positive_mbti': 'ESTJ',
    'negative_mbti': 'ESTP',
    },        
'INTP' : {
    'genre': '역사', 
    'keyword': ['비평', '아이디어', '직관', '객관적', '자연과학', '교수', '연구', '독창성'],
    'positive_mbti': 'ESFJ',
    'negative_mbti': 'ESFP',
    },        
'ESTP' : {
    'genre': '미스터리', 
    'keyword': ['도전', '모험', '어드벤쳐', '보물',  '스포츠', '자질', '이성', '과감'],
    'positive_mbti': 'INFJ',
    'negative_mbti': 'INFP',
    },        
'ESFP' : {
    'genre': '코미디', 
    'keyword': ['오락', '성인', '파티', '자극', '따뜻함', '디자인', '유쾌', '스타일'],
    'positive_mbti': 'INTJ',
    'negative_mbti': 'INTP',
    },         
'ENFP' : {
    'genre': '판타지', 
    'keyword': ['자유', '애니메이션', '로망', '동심', '재기발랄', '독립', '신비', '색다름'],
    'positive_mbti': 'ISTJ',
    'negative_mbti': 'ISTP',
    },        
'ENTP' : {
    'genre': '전쟁', 
    'keyword': ['패턴', '두뇌', '독립', '최신', '힙합', '입단', '지식', '증명'],
    'positive_mbti': 'ISFJ',
    'negative_mbti': 'ISFP',
    },                
'ESTJ' : {
    'genre': '범죄', 
    'keyword': [ '사업', '성공', '실용', '오피스', '상사', '신입사원', '정치인', '불가능'],
    'positive_mbti': 'INFP',
    'negative_mbti': 'INFJ',
    },        
'ESFJ' : {
    'genre': '음악', 
    'keyword': ['봉사', '협력', '친절', '조합', '조화', '응원', '화해', '예민'],
    'positive_mbti': 'ITNP',
    'negative_mbti': 'INTJ',
    },         
'ENFJ' : {
    'genre': '스릴러', 
    'keyword': ['카리스마', '지도자', '질서', '리더십', '언론', '코치', '감독', '교사'],
    'positive_mbti': 'ISTP',
    'negative_mbti': 'ISTJ',
    },        
'ENTJ' : {
    'genre': '공포', 
    'keyword':  ['완벽', '걸작', '거장', '부자', '부유', '왕', '장기', '권력'],
    'positive_mbti': 'ISFP',
    'negative_mbti': 'ISFJ',
    },    
}

# mbti keyword 반환
@api_view(['GET'])  
@permission_classes([AllowAny]) 
def mbti(request):
    return Response(MBTI_DICT)


# 내 mbti 추천
def get_my_movies(mbti, keyword_idx):
    genre_name = MBTI_DICT[mbti]['genre']
    keywords = []
    for idx in keyword_idx:
        keywords.append(MBTI_DICT[mbti]['keyword'][int(idx)])
    (key1, key2, key3, key4) = keywords
    #장르 영화
    genre = Genre.objects.get(name=genre_name)
    genre_movies = genre.movie_set.all()
    # 키워드 영화
    keyword_movies = Movie.objects.filter(
        Q(overview__contains=key1) |
        Q(overview__contains=key2) |
        Q(overview__contains=key3) |
        Q(overview__contains=key4))
    result = genre_movies | keyword_movies    
    # 둘의 합산값 return
    return result    

# mbti별 추천무비 쿼리셋 반환 메서드
def get_other_movies(mbti):
    genre_name = MBTI_DICT[mbti]['genre']
    (key1, key2, key3, key4) = random.sample(MBTI_DICT[mbti]['keyword'], 4)
    genre = Genre.objects.get(name=genre_name)
    #장르 영화
    genre_movies = genre.movie_set.all()
    # 키워드 영화
    keyword_movies = Movie.objects.filter(
        Q(overview__contains=key1) |
        Q(overview__contains=key2) |
        Q(overview__contains=key3) |
        Q(overview__contains=key4))
    result = genre_movies | keyword_movies
    # 둘의 합산값 return
    return result

# 전체 영화 
@api_view(['GET'])       
def take_movie(request):
    movies = Movie.objects.all()
    serializer = MovieTitleSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])       
def take_movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genre = movie.genres.all()
    serializer = MovieSerializer(movie)
    serializer2 = GenreSerializer(genre, many=True)
    serializer3 = movie.like_users.count()
    if movie.like_users.filter(username=request.user.username).exists():
        is_liking = True
    else:
        is_liking = False 
    return Response([serializer.data, serializer2.data, serializer3, is_liking])


@api_view(['GET'])    
def take_movie_search(request, keyword):
    title_movies = Movie.objects.filter(Q(title__contains=keyword))
    overview_movies = Movie.objects.filter(Q(overview__contains=keyword))
    # 영화 제목 
    serializer1 = MovieSerializer(title_movies, many=True)
    # 줄거리 포함
    serializer2 = MovieSerializer(overview_movies, many=True)
    return Response([serializer1.data, serializer2.data])


@api_view(['GET'])
def recommend_movies(request):
    user = get_object_or_404(get_user_model(), pk=request.user.pk)
    my_mbti = user.mbti
    # 파트너 mbti를 입력한 사람은 그 mbti로 , 아니면 궁합이 잘 맞는 mbti로
    if user.mbti_partner == 'solo':
        partner_mbti = MBTI_DICT[my_mbti]['positive_mbti']
    else:
        partner_mbti = user.mbti_partner
    negative_mbti = MBTI_DICT[my_mbti]['negative_mbti']
    # 아래 부분은 실제로 커로셀 구현 한 후에 다시 봐야 함
    # 나한테 잘 맞는것
    keywords = user.mbti_keywords
    my_movies = get_my_movies(my_mbti, keywords)
    my_result = my_movies.order_by('-vote_average')[0:10]
    # 파트너한테 잘 맞는 것
    partners_movies = get_other_movies(partner_mbti)
    partners_result = partners_movies.order_by('-vote_average')[0:10]
    # 둘다 한테 잘 맞는것
    together_movies = my_movies | partners_movies
    together_result = together_movies.order_by('-popularity')[0:10]
    # 나한테 상극인 것
    negative_movies = get_other_movies(negative_mbti)
    negative_result = negative_movies.order_by('-vote_average')[0:10]

    serializer1 = MovieSerializer(my_result, many=True)
    serializer2 = MovieSerializer(partners_result, many=True)
    serializer3 = MovieSerializer(together_result, many=True)
    serializer4 = MovieSerializer(negative_result, many=True)    

    return Response([serializer1.data, serializer2.data, serializer3.data, serializer4.data])

# 커뮤니티 전체 조회
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def community_list_create(request):
    if request.method == 'GET':
        communities = Community.objects.order_by('-pk')
        serializer = CommunitySerializer(communities, many=True)
        return Response(serializer.data)
    else:
        serializer = CommunitySerializer(data=request.data)
        movie = get_object_or_404(Movie, title=request.data['movie_title'])
        
        # 유효성 통과를 못함
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 특정 게시글 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def community_detail(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    serializer = CommunitySerializer(community)
    find_count = community.find_users.count()
    if community.find_users.filter(username=request.user.username).exists():
        is_finding = True
    else:
        is_finding = False

    return Response([serializer.data, find_count, is_finding])


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def community_update_delete(request, community_pk):
  community = get_object_or_404(Community, pk=community_pk)
  # 본인 글만 수정 가능
  if not request.user.communities.filter(pk=community_pk).exists():
    return Response({'message': '권한이 없습니다.'})
  if request.method == 'PUT':
      serializer = CommunitySerializer(community, data=request.data)
      movie = get_object_or_404(Movie, title=request.data['movie_title'])
      if serializer.is_valid(raise_exception=True):
          serializer.save(user=request.user, movie=movie)
          return Response(serializer.data)          
  else:
      community.delete()
      return Response({ 'id': community_pk })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def comment_list(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    comments = community.comment_set.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, community=community)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, community_pk, comment_pk):
  community = get_object_or_404(Community, pk=community_pk)
  comment = community.comment_set.get(pk=comment_pk)

  if not request.user.comments.filter(pk=comment_pk).exists():
    return Response({'message': '권한이 없습니다.'})
  else:
    comment.delete()
    return Response({ 'id': comment_pk })



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_list_create(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        reviews = movie.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    else:
        serializer = ReviewSerializer(data=request.data)
        movie = get_object_or_404(Movie, pk=movie_pk)
        # 유효성 통과를 못함
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def review_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = movie.review_set.get(pk=review_pk)

    if not request.user.reviews.filter(pk=review_pk).exists():
      return Response({'message': '권한이 없습니다.'})
        
    else:
      review.delete()
      return Response({ 'id': review_pk })



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def community_about_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    communities = movie.community_set.all()
    serializer = CommunitySerializer(communities, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk):
  movie = get_object_or_404(Movie, pk=movie_pk)
#   me = get_object_or_404(get_user_model(), username=username)
  if movie.like_users.filter(pk=request.user.pk).exists():
      movie.like_users.remove(request.user)
      liking = False
      
  else:
      movie.like_users.add(request.user)
      liking = True
  
  count = movie.like_users.count()
  return Response([liking, count])


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def finds(request, community_pk):
  community = get_object_or_404(Community, pk=community_pk)
#   me = get_object_or_404(get_user_model(), username=username)
  if community.find_users.filter(pk=request.user.pk).exists():
      community.find_users.remove(request.user)
      finding = False
      
  else:
      community.find_users.add(request.user)
      finding = True
  
  count = community.find_users.count()
  return Response([finding, count])


# 프로필 정보 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = get_object_or_404(get_user_model(), username=request.user.username)
    # 좋아요한 영화
    like_movies = user.like_movies.all()
    # 내가 작성한 리뷰
    reviews = user.reviews.all()
    # 내가 쓴 글
    communities = user.communities.all()
    # 내가 즐겨찾기 한 글
    find_communities = user.find_communities.all()

    serializer1 = MovieSerializer(like_movies, many=True)
    serializer2 = ReviewSerializer(reviews, many=True)
    serializer3 = CommunitySerializer(communities, many=True)
    serializer4 = CommunitySerializer(find_communities, many=True)
    return Response([serializer1.data, serializer2.data, serializer3.data, serializer4.data])


# 영화에서 내 좋아요 여부
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def is_movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(username=request.user.username).exists():
        is_like = True
    else:
        is_like = False
    return Response(is_like)