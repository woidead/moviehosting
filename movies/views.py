from django.shortcuts import render
from django.views.generic.base import View

from .models import Movie


class MovieView(View):
    """Спiсок фильмов"""
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies_html/movies.html', {'movie_list': movies})
    

class MovieDetailView(View):
    """Полное описание и детали к фильму"""
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'movies_html/movie_detail.html', {'movie':movie})