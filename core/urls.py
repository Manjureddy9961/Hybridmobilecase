from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('technology/', views.technology, name='technology'),
    path('analytics/', views.analytics, name='analytics'),
    path('battery/', views.battery, name='battery'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('profile/', views.profile, name='profile'),
    path('notifications/', views.notifications, name='notifications'),
    path('chatbot/response/', views.chatbot_response, name='chatbot_response'),
]
