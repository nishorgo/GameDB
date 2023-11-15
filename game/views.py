
from django.db.models import Count
from rest_framework.generics import ListCreateAPIView
from .models import Game, Publisher, Developer
from .serializers import GameSerializer, PublisherSerializer, DeveloperSerializer


class GameList(ListCreateAPIView):
    queryset = Game.objects.select_related('publisher', 'developer').all()
    serializer_class = GameSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    

class PublisherList(ListCreateAPIView):
    queryset = Publisher.objects.annotate(games_count=Count('games')).all()
    serializer_class = PublisherSerializer


class DeveloperList(ListCreateAPIView):
    queryset = Developer.objects.annotate(games_count=Count('games')).all()
    serializer_class = DeveloperSerializer