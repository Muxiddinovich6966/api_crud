from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import MovieCreateView, ActorCreateView, MovieViewSet

# from configapp.views import MovieApi, MovieDetailApi

# from .views import movie_list_create, movie_detail, MovieApi

router = DefaultRouter()
router.register(r'movies', MovieViewSet,basename="movie")
urlpatterns = [
      path('movie/<int:pk>/', MovieCreateView.as_view(), name='movie'),
      path('actor/<int:pk>/', ActorCreateView.as_view(), name='actor'),
      path('api/', include(router.urls)),
    # path("movies/", movie_list_create, name="movie-list-create"),
    # path("movies/",MovieApi.as_view()),
    # path("movies/<slug:slug>/",MovieDetailApi.as_view()),
    # path("movies/<slug:slug>/", movie_detail, name="movie-detail"),
]
