from supabase import create_client, Client

def get_user_id(email):
    data, count = supabase.table('users') \
        .select('id') \
        .eq('email', email) \
        .execute()
    id = data[1][0]['id']
    return id

def get_generation_id(user_id, title, description):
    data, count = supabase.table('generations') \
        .select('id') \
        .eq('user_id', user_id) \
        .eq('title', title) \
        .eq('description', description) \
        .execute()
    id = data[1][0]['id']
    return id

def generate_projects(preferences, options):
    data, count = supabase.table('users') \
        .select('id') \
        .eq('email', email) \
        .execute()
    id = data[1][0]['id']
    return id