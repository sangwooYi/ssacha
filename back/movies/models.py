from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.TextField()
    
    def __str__(self):
      return self.name


class Movie(models.Model):
    title = models.TextField()
    original_title = models.TextField()
    overview = models.TextField()
    # genres = models.ManyToManyField(Genre, related_name='movie_genre')
    genres = models.ManyToManyField(Genre)
    poster_path = models.TextField()
    vote_average = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    vote_count = models.IntegerField(validators=[MinValueValidator(0)])
    release_date = models.TextField()
    runtime = models.IntegerField(validators=[MinValueValidator(0)])
    popularity = models.FloatField(validators=[MinValueValidator(0)])
    adult = models.BooleanField()
    # 좋아요
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')


class Community(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="communities")
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE) # 얘를 넣어야 된단 
  title = models.CharField(max_length=100)
  content = models.TextField()
  rank = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  find_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='find_communities')

class Comment(models.Model):
  content = models.TextField()
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  community = models.ForeignKey(Community, on_delete=models.CASCADE)


class Review(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
  content = models.TextField()
  rank = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
