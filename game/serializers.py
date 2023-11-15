from rest_framework import serializers
from .models import Game, Publisher, Developer, Review


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


class GameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'release_date']
    

class GameDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'release_date', 'publisher', 'developer', 'description']

    publisher = serializers.HyperlinkedRelatedField(
        queryset=Publisher.objects.all(),
        view_name='publisher-detail'
    )
    developer = serializers.HyperlinkedRelatedField(
        queryset=Developer.objects.all(),
        view_name='developer-detail'
    )


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'rating', 'review_title', 'review_body', 'timestamp']

    def create(self, validated_data):
        game_id = self.context['game_id']
        return Review.objects.create(game_id=game_id, **validated_data)


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'rating', 'review_title', 'review_body', 'timestamp']
         