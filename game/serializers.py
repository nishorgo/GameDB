from rest_framework import serializers
from .models import Game, Publisher, Developer


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'country', 'games_count']

    games_count = serializers.IntegerField(read_only=True)


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ['id', 'name', 'country', 'games_count']

    games_count = serializers.IntegerField(read_only=True)
    

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'release_date', 'publisher', 'developer', 'platforms', 'description']

    # publisher = serializers.HyperlinkedRelatedField(
    #     queryset=Publisher.objects.all(),
    #     view_name='publisher-detail'
    # )
    # developer = serializers.HyperlinkedRelatedField(
    #     queryset=Developer.objects.all(),
    #     view_name='developer-detail'
    # )