from django.urls import path
from . import views


urlpatterns = [
    # 전체 영화
    path('take_movie/', views.take_movie),

    # 세부 영화 (movie_pk 검색)
    path('take_movie_detail/<int:movie_pk>', views.take_movie_detail),


    # 영화 검색 결과
    path('take_movie_search/<keyword>/', views.take_movie_search),

    # 영화 추천
    path('recommend_movies/', views.recommend_movies),

    # 게시글 작성
    path('community_list_create/', views.community_list_create), 
    path('detail/<int:community_pk>/', views.community_detail), 
    path('community/<int:community_pk>/', views.community_update_delete),

    # 게시글 즐겨찾기
    path('<int:community_pk>/finds/', views.finds),

    # 게시글 댓글
    path('comments/<int:community_pk>', views.comment_list),
    path('<int:community_pk>/comment/', views.create_comment),
    path('comment/<int:community_pk>/<int:comment_pk>/', views.comment_delete),


    # 영화 리뷰 작성
    path('<int:movie_pk>/review_list_create/', views.review_list_create),
    path('<int:movie_pk>/review/<int:review_pk>/', views.review_delete),

    # 상세페이지에서 영화 커뮤니티 조회
    path('<int:movie_pk>/community/', views.community_about_movie),

    #특정 영화 좋아요
    path('<int:movie_pk>/like/', views.movie_like),


    # 프로필 정보
    path('profile/', views.profile),


    # 영화에서 내 좋아요 여부
    path('is_movie_like/<int:movie_pk>/', views.is_movie_like),

    # mbti 키워드 전달
    path('mbti/', views.mbti)
]