import os
import openai
import requests
import json
from supabase import create_client, Client
import re

url = "https://hjymcwxdsalayjcsdvkt.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhqeW1jd3hkc2FsYXlqY3Nkdmt0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDMxMzkwMTMsImV4cCI6MjAxODcxNTAxM30.kSTCKTL1XIQop5jfow0F03EFY5yM-voLo6vz2qauJS8"
supabase = create_client(url, key)

"""
data, count = supabase.table('users').insert(
    {"first_name": "Emmett", "last_name": "Myers", "email": "emmettleemyers@gmail.com"}
).execute()
print(data)
print(count)

response = supabase.table('users').select("*").execute()
print(response)

data, count = supabase.table('generations').insert({
        "user_id": 5,
        "title": "test", 
        "description": "test", 
        "tools": ["test1", "test2"],
        "difficulty": "test",
        "time": "test"
    }).execute()
print(data)
print(count)

data, count = supabase.table('users').select('id').eq('email', 'emmettleemyers@gmail.com').execute()
print(data[1][0]['id'])
"""

query_test = "\
You are the engine behind an application that generates personal coding project ideas for aspiring software engineers who want unique and interesting project ideas. The users have their preferences saved, but also select options for the current app types they want to generate. Lean on their options selected, but if you need extra inspiration use their preferences. Come up with a list of 10 personal coding project ideas using their preferences and options selected. For each project idea, layout the 'Title', 'Coding Tools', a 1 paragraph 'Description', the 'Difficulty' based on their developer tools known and the tools of the current project, and estimated 'Time' based on their skills. Make sure the project ideas are unique and stand out in a resume as interesting and personalized.\
\n\nDeveloper Preferences\
\n----------------------------\
\nDeveloper broad project interests: websites, mobile apps, machine learning\
\nDeveloper tools known: HTML/CSS (advanced), Python (intermediate), Java (advanced), React (intermediate)\
\nDeveloper tools desired to learn: Vue, C#, .NET, Django\
\nDeveloper broad topic interests: sports, cats, computer science, gaming\
\n\nSpecific App Options Selected\
\n------------------------------------\
\nType of project: website\
\nPreferred difficulty based on developer skills: 3/5\
\nPreferred time to finish project: 2-3 weeks\
\nTools preferred to make the project: HTML/CSS, JavaScript, React\
\nPreferred topics for project: sports\
"
openai.organization = "org-B2VCzC8yPM5DdOCjJC0byQrm"
openai.api_key = "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"
openai.Model.list()
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + openai.api_key
}
data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": query_test}],
    "temperature": 0.7,
    "max_tokens": 2000
}
response = requests.post(url, headers=headers, data=json.dumps(data))
output = response.json()
content = output['choices'][0]['message']['content']
print(content + "\n\n------------------\n\n")

projects = content.split('\n\n')
project_list = []
for project in projects:
    lines = project.split('\n')
    project_dict = {}
    for line in lines:
        key, value = line.split(': ', 1)
        if ("Title" in key):
            key = key.split()[-1]
        project_dict[key] = value
    project_list.append(project_dict)

"""
for idx, project in enumerate(project_list, 1):
    print(f"Project {idx}:")
    for key, value in project.items():
        print(f"{key}: {value}")
    print("\n")
"""

print(project_list[9]['Coding Tools'])