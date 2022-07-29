from django.db import models

class Setting(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    value = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

class Movie(models.Model):
    def __init__(self, movie_info):
        self.title = movie_info.title
        self.tagline = movie_info.tagline
        self.overview = movie_info.overview
        self.poster_path = movie_info.poster_path
    def __str__(self):
        return self.title
    class Meta:
        managed = False
