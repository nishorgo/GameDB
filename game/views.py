from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Game, Publisher, Developer
from .serializers import GameSerializer, PublisherSerializer, DeveloperSerializer


class GameList(ListCreateAPIView):
    queryset = Game.objects.select_related('publisher', 'developer').all()
    serializer_class = GameSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    

class GameDetail(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.annotate(games_count=Count('games')).all()
    serializer_class = PublisherSerializer

    def destroy(self, request, *args, **kwargs):
        if Game.objects.filter(publisher=kwargs['pk']).count() > 0:
            return Response(
                {'error': 'Publisher can not be deleted because it is associated with one or more games.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().destroy(request, *args, **kwargs)
        

class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.annotate(games_count=Count('games')).all()
    serializer_class = DeveloperSerializer

    def destroy(self, request, *args, **kwargs):
        if Game.objects.filter(developer=kwargs['pk']).count() > 0:
            return Response(
                {'error': 'Developer can not be deleted because it is associated with one or more games.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return super().destroy(request, *args, **kwargs)