from django.urls import path, include
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('games', views.GameViewSet, basename='games')
router.register('publishers', views.PublisherViewSet)
router.register('developers', views.DeveloperViewSet)
router.register('platforms', views.PlatformViewSet)
router.register('genres', views.GenreViewSet, basename='genres')
router.register('audience', views.AudienceViewSet)
router.register('wishlist', views.WishListViewSet, basename='wishlist')
router.register('my-reviews', views.AudienceReviewViewSet, basename='my-reviews')

game_router = routers.NestedDefaultRouter(router, 'games', lookup='game')
game_router.register('reviews', views.ReviewViewset, basename='game-reviews')
game_router.register('images', views.GameImageViewSet, basename='game-images')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(game_router.urls))
]
