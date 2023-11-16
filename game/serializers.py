from rest_framework import serializers
from .models import Game, Publisher, Developer, Review, Audience, Wishlist, Platform


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
        fields = ['id', 'title', 'release_date', 'publisher', 'developer', 'description']

    publisher = serializers.HyperlinkedRelatedField(
        queryset=Publisher.objects.all(),
        view_name='publisher-detail'
    )
    developer = serializers.HyperlinkedRelatedField(
        queryset=Developer.objects.all(),
        view_name='developer-detail'
    )


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'rating', 'review_title', 'review_body', 'timestamp']

    def create(self, validated_data):
        game_id = self.context['game_id']
        user = self.context['user']
        return Review.objects.create(game_id=game_id, user=user, **validated_data)
    

class AudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audience
        fields = ['id', 'user', 'birth_date']
        read_only_fields = ['user']


class WishlistSerializer(serializers.ModelSerializer):
    # game = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all())

    game = serializers.HyperlinkedRelatedField(
        queryset=Publisher.objects.all(),
        view_name='games-detail'
    )

    class Meta:
        model = Wishlist
        fields = ['id', 'game', 'timestamp']

    def create(self, validated_data):
        user = self.context.get('user')
        return Wishlist.objects.create(user=user, **validated_data)
    

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['id', 'name', 'owner', 'games_count', 'launch_date']

    games_count = serializers.IntegerField(read_only=True)

         