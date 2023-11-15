from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.GameList.as_view()),
    path('games/<int:pk>', views.GameDetail.as_view()),
    path('publishers/', views.PublisherList.as_view()),
    path('publishers/<int:pk>', views.PublisherDetail.as_view(), name='publisher-detail'),
    path('developers/', views.DeveloperList.as_view()),
    path('developer/<int:pk>', views.DeveloperDetail.as_view(), name='developer-detail'),
]
