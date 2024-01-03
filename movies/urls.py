from django.urls import path
from  movies import views

urlpatterns = [
    path('', views.MovieView.as_view(), name='main'),
    path('<slug:slug>', views.MovieDetailView.as_view(), name='movie_detail')
]