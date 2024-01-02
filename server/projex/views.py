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
    email = data.get('email')
    # check if user is new to site
    if (is_user_new(supabase, email)):
        # add user to users table
        data, count = supabase.table('users').insert({
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
    user_id = email_to_user_id(supabase, email)
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
    user_id = email_to_user_id(supabase, email)
    data, count = supabase.table('preferences') \
        .update({
            'project_interests': project_interests,
            'tools_known': tools_known,
            'tools_desired_to_learn': tools_desired_to_learn,
            'topic_interests': topic_interests,
        }).eq('user_id', user_id) \
        .execute()
    return JsonResponse(data, safe=False)

@csrf_exempt
def get_past_generations(request):
    data = json.loads(request.body)
    email = data.get('email')
    user_id = email_to_user_id(supabase, email)
    data, count = supabase.table('generations').select('*').eq('user_id', user_id).execute()
    return JsonResponse(data, safe=False)

@csrf_exempt
def get_project_generations(request):
    data = json.loads(request.body)
    email = data.get('email')
    user_id = email_to_user_id(supabase, email)
    preferences_data, count = supabase.table('preferences').select('*').eq('user_id', user_id).execute()
    preferences = preferences_data[1][0]
    options = data.get('options')
    while True:
        generated_projects = generate_projects(preferences, options)
        # check if all projects have the required keys
        if all(project_has_required_keys(project) for project in generated_projects):
            break  # exit the loop
    for project in generated_projects:
        add_generation(user_id, project)
    return JsonResponse(generated_projects, safe=False)

@csrf_exempt
def add_generation(user_id, project):
    data, count = supabase.table('generations').insert({
        "user_id": user_id,
        "title": project['Title'], 
        "description": project['Description'], 
        "tools": project['Coding Tools'],
        "difficulty": project['Difficulty'],
        "time": project['Time']
    }).execute()
    return JsonResponse(data, safe=False)

@csrf_exempt
def get_saved_projects(request):
    data = json.loads(request.body)
    email = data.get('email')
    user_id = email_to_user_id(supabase, email)
    saved_projects = []
    saved, count = supabase.table('saved_projects').select('generation_id').eq('user_id', user_id).execute()
    for generation in saved[1]:
        data, count = supabase.table('generations') \
            .select('*') \
            .eq('id', generation['generation_id']) \
            .execute()
        project = data[1][0]
        saved_projects.append(project)
    return JsonResponse(saved_projects[::-1], safe=False)

@csrf_exempt
def add_saved_project(request):
    data = json.loads(request.body)
    email = data.get('email')
    title = data.get('title')
    description = data.get('description')
    user_id = email_to_user_id(supabase, email)
    generation_id = user_id_to_generation_id(supabase, user_id, title, description)
    data, count = supabase.table('saved_projects').insert({
        "user_id": user_id,
        "generation_id": generation_id
    }).execute()
    return JsonResponse(data, safe=False)

@csrf_exempt
def delete_saved_project(request):
    data = json.loads(request.body)
    email = data.get('email')
    title = data.get('title')
    description = data.get('description')
    user_id = email_to_user_id(supabase, email)
    generation_id = user_id_to_generation_id(supabase, user_id, title, description)
    data, count = supabase.table('saved_projects') \
        .delete() \
        .eq('user_id', user_id) \
        .eq('generation_id', generation_id) \
        .execute()
    return JsonResponse(data, safe=False)

@csrf_exempt
def get_project_pool(request):
    data = json.loads(request.body)
    email = data.get('email')
    user_id = email_to_user_id(supabase, email)
    saved, count = supabase.table('saved_projects').select('generation_id').eq('user_id', user_id).execute()
    saved_generation_ids = [entry['generation_id'] for entry in saved[1]]
    project_pool = []
    data, count = supabase.table('generations').select('*').execute()
    for generation in data[1]:
        if len(project_pool) <= 50:
            if generation['id'] not in saved_generation_ids:
                project_pool.append(generation)
    return JsonResponse(project_pool, safe=False)
