from django_filters.rest_framework import FilterSet
from .models import Review

class ReviewFilter(FilterSet):
    class Meta:
        model = Review
        fields = {
            'rating': ['gte', 'lte']
        }