from django_filters.rest_framework import FilterSet
from .models import Review, Game

class ReviewFilter(FilterSet):
    class Meta:
        model = Review
        fields = {
            'rating': ['gte', 'lte']
        }

class GameFilter(FilterSet):
    class Meta:
        model = Game
        fields = {
            'publisher_id': ['exact'],
            'developer_id': ['exact'],
            'average_rating': ['gte', 'lte']
        }