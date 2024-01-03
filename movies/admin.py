from django.contrib import admin

from .models import Category, Actors, Genre, Movie, MovieShots, RatingStar, Rating, Reviews

admin.site.register(Category)
admin.site.register(Actors)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)