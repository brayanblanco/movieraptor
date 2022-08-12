from django.urls import path

from . import views

app_name = "movies"
urlpatterns = [
    path('<int:movie_id>/', views.detail, name='detail'),
    path('search/<str:search_terms>/<int:page>/', views.search, name='search')
]
