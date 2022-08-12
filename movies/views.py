import tmdbsimple as tmdb

from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from . import moviehelper

def detail(request, movie_id):
    movie = moviehelper.get_movie_by_id(movie_id)
    return render(request, "movies/detail.html", {'movie': movie})

def search(request, search_terms, page):
    movie_list = moviehelper.search_movies(search_terms, page)
    previous_page = None if (page == 1) else page - 1
    next_page = None if (page == movie_list.total_pages) else page + 1

    return render(request, "movies/search.html", {'movie_list': movie_list.movies, 'search_terms':search_terms, 'previous_page':previous_page, 'next_page': next_page})
