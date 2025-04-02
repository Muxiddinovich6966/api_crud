from django.urls import path
from .views import movie_list_create, movie_detail

urlpatterns = [
    path("movies/", movie_list_create, name="movie-list-create"),
    path("movies/<slug:slug>/", movie_detail, name="movie-detail"),
]


