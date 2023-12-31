from django.urls import path
from . import views

urlpatterns = [
    path('connection_test/', views.connection_test, name='connection_test'),
    path('add_new_user/', views.add_new_user, name='add_new_user'), # used
    path('get_preferences/', views.get_preferences, name='get_preferences'), # used
    path('update_preferences/', views.update_preferences, name='update_preferences'), # used
    path('get_project_generations/', views.get_project_generations, name='get_project_generations'),
    path('get_saved_projects/', views.get_saved_projects, name='get_saved_projects'),
    path('add_saved_project/', views.add_saved_project, name='add_saved_project'),
    path('delete_saved_project/', views.delete_saved_project, name='delete_saved_project'),
]
