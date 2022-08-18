from rest_framework import serializers
from .models import Movie, Comment, Review, Community, Genre


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Movie
        fields = '__all__'
        # extra_fields = ['genres_titles']
        # fields = ('id', 'title', 'overview', 'genres', 'poster_path', 'vote_average', 'release_date', 'runtime', 'adult', 'popularity', 'adult', 'like_users', 'genres_titles')

class MovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
      model = Movie
      fields = ('id', 'title',)


class CommunitySerializer(serializers.ModelSerializer):
  userName = serializers.SerializerMethodField()
  mbti = serializers.SerializerMethodField()

  def get_userName(self,obj):
    return obj.user.username

  def get_mbti(self, obj):
    return obj.user.mbti

  movie_title = serializers.SerializerMethodField()
  poster_path = serializers.SerializerMethodField()
  
  def get_movie_title(self, obj):
    return obj.movie.title

  def get_poster_path(self, obj):
    return obj.movie.poster_path

  class Meta:
    model = Community
    # fields = "__all__"
    fields = ('id', 'user', 'userName',  'title', 'movie_title', 'content', 'created_at', 'updated_at', 'poster_path', 'mbti', 'find_users', 'rank')
    read_only_fields = ('user', 'find_users')



class CommentSerializer(serializers.ModelSerializer):
  userName = serializers.SerializerMethodField()
  
  def get_userName(self,obj):
    return obj.user.username

  class Meta:
    model = Comment
    fields = ('id', 'user', 'userName', 'content', 'created_at', 'updated_at', 'community',)
    read_only_fields = ('user','community',)



class ReviewSerializer(serializers.ModelSerializer):
  userName = serializers.SerializerMethodField()
  mbti = serializers.SerializerMethodField()

  def get_userName(self,obj):
    return obj.user.username

  def get_mbti(self, obj):
    return obj.user.mbti

  class Meta:
    model = Review
    fields = ('id', 'user', 'userName', 'content', 'movie', 'rank', 'created_at', 'updated_at', 'mbti')
    read_only_fields = ('user', 'movie')
      



# class CommunitySerializer(serializers.ModelSerializer):
#   userName = serializers.SerializerMethodField()
  
#   def get_userName(self,obj):
#     return obj.user.username

#   class Meta:
#     model = Community
#     fields = ('id', 'user', 'title', 'content', 'created_at', 'updated_at',)
#     # userName
#     read_only_fields = ('user',)




# class CommentSerializer(serializers.ModelSerializer):
#   userName = serializers.SerializerMethodField()
  
#   def get_userName(self,obj):
#     return obj.user.username

#   class Meta:
#     model = Comment
#     fields = ('id', 'user', 'content', 'created_at', 'updated_at', 'community',)
#     read_only_fields = ('user','community',)



# class ReviewSerializer(serializers.ModelSerializer):
#   movie_title = serializers.SerializerMethodField()

#   def get_movie_title(self, obj):
#     return obj.movie.title

#   userName = serializers.SerializerMethodField()
  
#   def get_userName(self,obj):
#     return obj.user.username

#   class Meta:
#     model = Review
#     fields = ('id', 'user', 'title', 'content', 'movie', 'rank', 'created_at', 'updated_at', 'movie_title')
#     read_only_fields = ('user',)