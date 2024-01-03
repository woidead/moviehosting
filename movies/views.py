from django.shortcuts import render
from django.views.generic import  ListView, DetailView

from .models import Movie


class MovieView(ListView):
    """Спiсок фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies/movies.html' #это нужно для того чтобы джанго находил путь на авто. он к имени модели добавляет _list

class MovieDetailView(DetailView):
    """Полное описание и детали к фильму"""
    model = Movie
    slug_field = 'url' 
    #тут уже _detail и поэтому не нужен template_name
    