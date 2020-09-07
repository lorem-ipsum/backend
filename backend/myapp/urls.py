from django.urls import path

from . import views

urlpatterns = [
    path('movies/', views.movies),
    path('characters/', views.characters),
]
