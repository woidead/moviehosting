from django.db import models
from datetime import date
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    """Категории"""
    name = models.CharField('Категория', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actors(models.Model):
    """Актеры и режиссеры"""
    name = models.CharField('Имя актера', max_length=150)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='actors/')

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"

class Genre(models.Model):
    """Жанры"""
    name = models.CharField('Категория', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    
class Movie(models.Model):
    """Фильмы"""
    title = models.CharField('Название', max_length=100)
    tagline = models.CharField('Слоган', max_length=100)
    description = models.TextField('Описание')
    poster = models.ImageField("Постер", upload_to='posters/')
    year = models.PositiveSmallIntegerField("Год выхода", default=2023)
    country = models.CharField("Страна", max_length=100)
    directions = models.ManyToManyField(Actors, verbose_name='Режиссеры', related_name='film_director')
    actors = models.ManyToManyField(Actors, verbose_name='Актеры', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')
    world_premiere = models.DateField("Премьера в мире", default=date.today)
    budget =  models.PositiveIntegerField("Бюджет фильма", default=0, help_text="Указывать в долларах")
    feels_in_usa = models.PositiveIntegerField("Сборы в США", default=0, help_text="Указывать в долларах")
    feels_in_world = models.PositiveIntegerField("Сборы в мире", default=0, help_text="Указывать в долларах")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug':self.url})


class MovieShots(models.Model):
    """Кадры из фильма"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"

class RatingStar(models.Model):
    """Звезды рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)
    def __str__(self) -> str:
        return self.value
    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

class Rating(models.Model):
    """Рейтинги"""
    ip = models.CharField("IP адресс", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм")
    def __str__(self) -> str:
        return f'{self.star}-{self.value}' 
    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """"""
    email = models.EmailField()
    name = models.CharField('Имя', max_length=150)
    text = models.TextField('Сообщение')
    parents = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.star}-{self.value}' 
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"