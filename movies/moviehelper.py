import tmdbsimple as tmdb

from  requests.exceptions import HTTPError

from .models import Setting, Movie

try:
    tmdb.API_KEY = Setting.objects.get(name='API_KEY').value
except Setting.DoesNotExist:
    raise Exception("The API_KEY setting is not set")

def get_movie_by_id(movie_id):
    info = tmdb.Movies(movie_id)
    info.info()
    movie = Movie.from_movie_info(info)

    return movie

def search_movies(search_terms):
    search = tmdb.Search()
    search.movie(query = search_terms)

    movies = []
    for movie in search.results:
        movies.append(Movie(movie["id"], movie["title"]))

    return movies
