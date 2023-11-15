from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('publishers', views.PublisherViewSet)
router.register('developers', views.DeveloperViewSet)

urlpatterns = [
    path('games/', views.GameList.as_view()),
    path('games/<int:pk>', views.GameDetail.as_view()),
] + router.urls
