from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
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
    

class PublisherList(ListCreateAPIView):
    queryset = Publisher.objects.annotate(games_count=Count('games')).all()
    serializer_class = PublisherSerializer


class PublisherDetail(RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def delete(self, request, pk):
        publisher = get_object_or_404(Publisher, pk=pk)
        if publisher.games.count() > 0:
            return Response(
                {'error': 'Publisher can not be deleted because it is associated with one or more games.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class DeveloperList(ListCreateAPIView):
    queryset = Developer.objects.annotate(games_count=Count('games')).all()
    serializer_class = DeveloperSerializer


class DeveloperDetail(RetrieveUpdateDestroyAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

    def delete(self, request, pk):
        developer = get_object_or_404(Developer, pk=pk)
        if developer.games.count() > 0:
            return Response(
                {'error': 'Developer can not be deleted because it is associated with one or more games.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        developer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)