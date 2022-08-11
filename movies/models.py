from django.db import models

class Setting(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    value = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

class Movie(models.Model):
    def __init__(self, id, title):
        self.id = id
        self.title = title

    @classmethod
    def from_movie_info(cls, movie_info):
        movie = cls(movie_info.id, movie_info.title)
        movie.tagline = movie_info.tagline
        movie.overview = movie_info.overview
        movie.poster_path = movie_info.poster_path
        return movie

    def __str__(self):
        return self.title
    class Meta:
        managed = False
