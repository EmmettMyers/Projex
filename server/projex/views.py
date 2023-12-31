from rest_framework.parsers import JSONParser
from supabase import create_client, Client
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializer import UserSerializer, PreferenceSerializer, GenerationSerializer, SavedProjectSerializer
from .models import User, Preference, Generation, SavedProject
from .utils import *

supabase_url = {URL}
supabase_key = {KEY}
supabase = create_client(supabase_url, supabase_key)

@csrf_exempt
def connection_test(request):
    return HttpResponse("Connected")

@csrf_exempt
def add_new_user(request):
    data = json.loads(request.body)
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    # check if user is new to site
    if (is_user_new(supabase, email)):
        # add user to users table
        data, count = supabase.table('users').insert({
            "first_name": first_name, 
            "last_name": last_name, 
            "email": email
        }).execute()
        # add user to preferences table
        user_id = data[1][0]['id']
        data, count = supabase.table('preferences').insert({
            "user_id": user_id,
            "project_interests": [], 
            "tools_known": [], 
            "tools_desired_to_learn": [],
            "topic_interests": [],
        }).execute()
        return JsonResponse(data, safe=False)
    return HttpResponse("User already exists in database.")

@csrf_exempt
def get_preferences(request):
    data = json.loads(request.body)
    email = data.get('email')
    user_id = get_user_id(supabase, email)
    data, count = supabase.table('preferences').select('*').eq('user_id', user_id).execute()
    return JsonResponse(data, safe=False)

@csrf_exempt
def update_preferences(request):
    data = json.loads(request.body)
    email = data.get('email')
    project_interests = data.get('projectInterests')
    tools_known = data.get('toolsKnown')
    tools_desired_to_learn = data.get('toolsDesiredToLearn')
    topic_interests = data.get('topicInterests')
    user_id = get_user_id(supabase, email)
    data, count = supabase.table('preferences') \
        .update({
            'project_interests': project_interests,
            'tools_known': tools_known,
            'tools_desired_to_learn': tools_desired_to_learn,
            'topic_interests': topic_interests,
        }).eq('user_id', user_id) \
        .execute()
    return JsonResponse(data, safe=False)

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
