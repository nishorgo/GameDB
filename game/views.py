from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import status, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .filters import ReviewFilter
from .models import Game, Publisher, Developer, Review
from .serializers import GameListSerializer, GameDetailSerializer, PublisherSerializer, DeveloperSerializer, ReviewListSerializer, ReviewDetailSerializer


class GameList(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['publisher_id', 'developer_id']
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'rating', 'release_date']

    def get_serializer_context(self):
        return {'request': self.request}
    

class GameCreate(generics.CreateAPIView):
    serializer_class = GameDetailSerializer
    

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.select_related('publisher', 'developer').all()
    serializer_class = GameDetailSerializer


class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ReviewFilter
    ordering_fields = ['title', 'rating', 'release_date']


    def get_queryset(self):
        return Review.objects.filter(game_id=self.kwargs['pk'])
    
    def get_serializer_context(self):
        return {'game_id': self.kwargs['pk']}
    

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    lookup_url_kwarg = 'review'
    


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.annotate(games_count=Count('games')).all()
    serializer_class = PublisherSerializer

    def destroy(self, request, *args, **kwargs):
        if Game.objects.filter(publisher=kwargs['pk']).count() > 0:
            return Response(
                {'error': 'Publisher can not be deleted because it is associated with one or more games.'}, 
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )

        return super().destroy(request, *args, **kwargs)
        

class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.annotate(games_count=Count('games')).all()
    serializer_class = DeveloperSerializer

    def destroy(self, request, *args, **kwargs):
        if Game.objects.filter(developer=kwargs['pk']).count() > 0:
            return Response(
                {'error': 'Developer can not be deleted because it is associated with one or more games.'}, 
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
        
        return super().destroy(request, *args, **kwargs)
    