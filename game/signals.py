from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Audience, Review
from django.db import models


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_audience_for_new_user(sender, **kwargs):
    if kwargs['created']:
        Audience.objects.create(user=kwargs['instance'])

@receiver(post_save, sender=Review)
def update_game_average_rating(sender, instance, **kwargs):
    game = instance.game
    queryset = Review.objects.filter(game=game)
    total_ratings = queryset.aggregate(total_ratings=models.Sum('rating'))['total_ratings']
    total_reviews = queryset.count()

    if total_reviews > 0:
        new_average_rating = total_ratings / total_reviews
        game.average_rating = new_average_rating
        game.save()