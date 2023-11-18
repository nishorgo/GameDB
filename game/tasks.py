from datetime import datetime, timedelta
from django.db.models import Count
from .models import Game
from celery import shared_task


@shared_task
def find_trending_games():
    one_month_ago = datetime.now() - timedelta(days=30)

    trending_games = Game.objects.filter(release_date__gte=one_month_ago).annotate(
        reviews_count=Count('reviews')
    ).order_by('-reviews_count')