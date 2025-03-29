from django.contrib import admin
from django.urls import path

from configapp.views import *

urlpatterns = [
    path('movie_list_create/', movie_list_create),
    path('movie_detail/<slug:slug>/', movie_detail),


]
