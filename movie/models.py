from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Actor(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    birthdate = models.DateField()
    gender = models.CharField(max_length=6)


class Movie(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    year = models.IntegerField()
    imdb = models.URLField()
    genre = models.CharField(max_length=50)
    actor = models.ManyToManyField(Actor)


class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
