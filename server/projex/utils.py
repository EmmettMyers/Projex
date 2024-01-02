from supabase import create_client, Client
import openai
import requests
import json

openai_org = {ORG}
openai_key = {KEY}

def is_user_new(supabase, email):
    data, count = supabase.table('users') \
        .select('id') \
        .eq('email', email) \
        .execute()
    return True if len(data[1]) == 0 else False

def email_to_user_id(supabase, email):
    data, count = supabase.table('users') \
        .select('id') \
        .eq('email', email) \
        .execute()
    id = data[1][0]['id']
    return id

def user_id_to_generation_id(supabase, user_id, title, description):
    data, count = supabase.table('generations') \
        .select('id') \
        .eq('user_id', user_id) \
        .eq('title', title) \
        .eq('description', description) \
        .execute()
    id = data[1][0]['id']
    return id

def generate_projects(preferences, options):
    # developer preferences, string form
    project_interests = ", ".join(preferences['project_interests'])
    tools_known = ", ".join(preferences['tools_known'])
    tools_desired_to_learn = ", ".join(preferences['tools_desired_to_learn'])
    topic_interests = ", ".join(preferences['topic_interests'])

    # selected generation options, string form
    type = ", ".join(options['type'])
    difficulty = ", ".join(options['difficulty'])
    time = ", ".join(options['time'])
    tools = ", ".join(options['tools'])
    topics = ", ".join(options['topics'])

    # gpt query
    query_intro = "You are the engine behind an application that generates personal coding project ideas for aspiring software engineers who want unique and interesting project ideas. The users have their preferences saved, but also select options for the current app types they want to generate. Lean on their options selected, but if you need extra inspiration use their preferences. Come up with a list of 10 personal coding project ideas using their preferences and options selected. For each project idea, layout the 'Title', 'Coding Tools', a 1 paragraph 'Description', the 'Difficulty' based on their developer tools known and the tools of the current project, and estimated 'Time' based on their skills. Make sure the project ideas are unique and stand out in a resume as interesting and personalized."
    query_preferences = '\n\nDeveloper Preferences' + \
                        '\n---------------------' + \
                        '\nDeveloper broad project interests: ' + project_interests + \
                        '\nDeveloper tools known: ' + tools_known + \
                        '\nDeveloper tools desired to learn: ' + tools_desired_to_learn + \
                        '\nDeveloper broad topic interests: ' + topic_interests
    query_options = '\n\nSpecific App Options Selected' + \
                    '\n-----------------------------' + \
                    '\nType of project: ' + type + \
                    '\nPreferred difficulty based on developer skills: ' + difficulty + \
                    '\nPreferred time to finish project: ' + time + \
                    '\nTools preferred to make the project: ' + tools + \
                    '\nPreferred topics for project: ' + topics
    query = query_intro + query_preferences + query_options

    # send query to gpt turbo model
    openai.organization = openai_org
    openai.api_key = openai_key
    openai.Model.list()
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + openai.api_key
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": query}],
        "temperature": 0.7,
        "max_tokens": 2000
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    output = response.json()
    content = output['choices'][0]['message']['content']

    # parse content into map
    projects = content.split('\n\n')
    project_list = []
    for project in projects:
        lines = project.split('\n')
        project_dict = {}
        for line in lines:
            key, value = line.split(': ', 1)
            if ("Title" in key):
                key = key.split()[-1]
                value = value.strip('"')
            if (key == "Coding Tools"):
                value = value.split(',')
                for i in range(len(value)):
                    value[i] = value[i].lstrip()
            project_dict[key] = value
        project_list.append(project_dict)

    return project_list
