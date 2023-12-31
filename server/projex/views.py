from rest_framework.parsers import JSONParser
from supabase import create_client, Client
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializer import UserSerializer, PreferenceSerializer, GenerationSerializer, SavedProjectSerializer
from .models import User, Preference, Generation, SavedProject
from utils import *

url = {URL}
key = {KEY}
supabase = create_client(url, key)

def add_new_user(request):
    # add user to users table
    data, count = supabase.table('users').insert({
        "first_name": request.first_name, 
        "last_name": request.last_name, 
        "email": request.email
    }).execute()
    # add user to preferences table
    user_id = data[1][0]['id']
    data, count = supabase.table('preferences').insert({
        "user_id": user_id,
        "project_interests": [''], 
        "tools_known": [''], 
        "tools_desired_to_learn": [''],
        "topic_interests": [''],
    }).execute()
    return JsonResponse(data)

def get_preferences(request):
    user_id = get_user_id(request.email)
    data, count = supabase.table('preferences').select('*').eq('user_id', user_id).execute()
    return JsonResponse(data)

def update_preferences(request):
    user_id = get_user_id(request.email)
    data, count = supabase.table('preferences') \
        .update(request) \
        .eq('user_id', user_id) \
        .execute()
    return JsonResponse(data)

def get_project_generations(request):
    user_id = get_user_id(request.email)
    preferences = get_preferences(request)
    options = request.options
    generated_projects = generate_projects(preferences, options)
    for project in generated_projects:
        add_generation(user_id, project)
    return JsonResponse(generated_projects)

def add_generation(user_id, project):
    data, count = supabase.table('generations').insert({
        "user_id": user_id,
        "title": project['Title'], 
        "description": project['Description'], 
        "tools": project['Coding Tools'],
        "difficulty": project['Difficulty'],
        "time": project['Time']
    }).execute()
    return JsonResponse(data)

def get_saved_projects(request):
    user_id = get_user_id(request.email)
    data, count = supabase.table('saved_projects').select('*').eq('user_id', user_id).execute()
    return JsonResponse(data)

def add_saved_project(request):
    user_id = get_user_id(request.email)
    generation_id = get_generation_id(user_id, request.title, request.description)
    data, count = supabase.table('saved_projects').insert({
        "user_id": user_id,
        "generation_id": generation_id
    }).execute()
    return JsonResponse(data)

def delete_saved_project(request):
    user_id = get_user_id(request.email)
    generation_id = get_generation_id(user_id, request.title, request.description)
    data, count = supabase.table('saved_projects') \
        .delete() \
        .eq('user_id', user_id) \
        .eq('generation_id', generation_id) \
        .execute()
    return JsonResponse(data)