import os
from supabase import create_client, Client

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