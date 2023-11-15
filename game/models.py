from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=255)
    launch_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    average_rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(10.0)])

    publisher = models.ForeignKey(Publisher, on_delete=models.RESTRICT, related_name='games')
    developer = models.ForeignKey(Developer, on_delete=models.RESTRICT, related_name='games')

    platforms = models.ManyToManyField(Platform, through='GamePlatform')

    def __str__(self):
        return self.title


class GamePlatform(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.game.title + ' - ' + self.platform.name

# # class CustomUser(AbstractUser):
# #     birth_date = models.DateField(null=True, blank=True)
# #     profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

# # class Review(models.Model):
# #     game = models.ForeignKey(Game, on_delete=models.CASCADE)
# #     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
# #     rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
# #     review_title = models.CharField(max_length=255)
# #     review_body = models.TextField()
# #     timestamp = models.DateTimeField(auto_now_add=True)

# # class Wishlist(models.Model):
# #     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
# #     game = models.ForeignKey(Game, on_delete=models.CASCADE)
# #     timestamp = models.DateTimeField(auto_now_add=True)