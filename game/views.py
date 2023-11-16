from django.shortcuts import get_object_or_404
from django.db.models import Count

from rest_framework.decorators import action
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .filters import ReviewFilter
from .models import Game, Publisher, Developer, Review, Audience
from .serializers import GameSerializer, PublisherSerializer, DeveloperSerializer, ReviewSerializer, AudienceSerializer
from .permissions import IsAdminOrReadOnly, IsReviewOwnerOrAdmin, IsReadAndUpdateAndDelete


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.select_related('publisher', 'developer').all()
    serializer_class = GameSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['publisher_id', 'developer_id']
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'average_rating', 'release_date']

    def get_serializer_context(self):
        return {'request': self.request}
    

class ReviewViewset(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ReviewFilter
    ordering_fields = ['rating', 'timestamp']
    
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated(), IsReviewOwnerOrAdmin()]

    def get_queryset(self):
        return Review.objects.filter(game_id=self.kwargs.get('game_pk'))
    
    def get_serializer_context(self):
        if self.request.user.is_authenticated:
            audience = Audience.objects.get(user_id=self.request.user.id)
        else: audience = None
        return {'game_id': self.kwargs.get('game_pk'), 'user': audience}
    

class AudienceReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['rating', 'timestamp']
    permission_classes = [IsReadAndUpdateAndDelete]
    
    def get_queryset(self):
        audience = get_object_or_404(Audience, user_id=self.request.user.id)
        return Review.objects.filter(user=audience)


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
    

class AudienceViewSet(viewsets.ModelViewSet):
    queryset = Audience.objects.all()
    serializer_class = AudienceSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
         
        audience = Audience.objects.get(user_id=request.user.id)
        if request.method == 'GET':
            serializer = AudienceSerializer(audience)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = AudienceSerializer(audience, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)