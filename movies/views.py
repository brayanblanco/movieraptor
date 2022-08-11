import tmdbsimple as tmdb

from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from . import moviehelper

def detail(request, movie_id):
    movie = moviehelper.get_movie_by_id(movie_id)
    return render(request, "movies/detail.html", {'movie': movie})

def search(request, search_terms):
    movie_list = moviehelper.search_movies(search_terms)
    return render(request, "movies/search.html", {'movie_list': movie_list})
