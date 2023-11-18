from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from .validators import validate_file_size


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255, null=True)
    launch_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-launch_date']

    def __str__(self):
        return self.name
    

class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    origin_date = models.DateField(null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    average_rating = models.FloatField(null=True, validators=[MinValueValidator(1.0), MaxValueValidator(10.0)])

    publisher = models.ForeignKey(Publisher, on_delete=models.RESTRICT, related_name='games')
    developer = models.ForeignKey(Developer, on_delete=models.RESTRICT, related_name='games')

    platforms = models.ManyToManyField(Platform, through='GamePlatform')
    genres = models.ManyToManyField(Genre, through='GameGenre')

    class Meta:
        ordering = ['-release_date']

    def __str__(self):
        return self.title
    

class GameImage(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='game/images', validators=[validate_file_size])


class GamePlatform(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.game.title + ' - ' + self.platform.name
    
class GameGenre(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.game.title + ' - ' + self.genre.name
    

class Audience(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name}'


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(Audience, on_delete=models.SET_NULL, null=True, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    review_title = models.CharField(max_length=255)
    review_body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-rating']

    def __str__(self):
        return self.review_title


class Wishlist(models.Model):
    user = models.ForeignKey(Audience, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='wishlists')
    timestamp = models.DateTimeField(auto_now_add=True)