from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.GameList.as_view()),
    path('publishers/', views.PublisherList.as_view()),
    # path('publishers/<int:pk>', views.publisher_detail, name='publisher-detail'),
    path('developers/', views.DeveloperList.as_view()),
    # path('developer/<int:pk>', views.developer_detail, name='developer-detail'),
]
