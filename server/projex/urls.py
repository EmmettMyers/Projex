from django.urls import path
from . import views

urlpatterns = [
    path('add_user/', views.add_user, name='add_user'),
    path('add_generation/', views.add_generation, name='add_generation'),
]