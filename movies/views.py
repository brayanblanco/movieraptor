import tmdbsimple as tmdb
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Setting, Movie

def index(request):
    return HttpResponse("It's Alive!!")

def detail(request, movie_id):
    try:
        setting = Setting.objects.get(name='API_KEY')
    except Setting.DoesNotExist:
        return HttpResponse("TMDb API key is not set")

    tmdb.API_KEY = setting.value
    movie_info = tmdb.Movies(movie_id)
    movie_info.info()
    movie = Movie(movie_info)
    return render(request, "movies/detail.html", {'movie': movie})
    #return HttpResponse(movie.title)
