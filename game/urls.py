from django.urls import path, include
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('publishers', views.PublisherViewSet)
router.register('developers', views.DeveloperViewSet)


urlpatterns = [
    path('games/', views.GameList.as_view()),
    path('games/create/', views.GameCreate.as_view()),
    path('games/<int:pk>/', views.GameDetail.as_view()),
    path('games/<int:pk>/reviews/', views.ReviewList.as_view()),
    path('games/<int:pk>/reviews/<int:review>/', views.ReviewDetail.as_view()),
] + router.urls
