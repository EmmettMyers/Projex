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
    # developer preferences, string form
    project_interests = ", ".join(preferences.project_interests)
    tools_known = ", ".join(preferences.tools_known)
    tools_desired_to_learn = ", ".join(preferences.tools_desired_to_learn)
    topic_interests = ", ".join(preferences.topic_interests)

    # selected generation options, string form
    type = options.type
    difficulty = options.difficulty
    time = options.time
    tools = ", ".join(options.tools)
    topics = ", ".join(options.topics)

    # gpt query
    query_intro = 'You are the engine behind an application that generates personal coding project ideas for aspiring software engineers who want unique and interesting project ideas. The users have their preferences saved, but also select options for the current app types they want to generate. Lean on their options selected, but if you need extra inspiration use their preferences. Come up with a list of 10 personal coding project ideas using their preferences and options selected. For each project idea, layout the title, coding tools used, a 1 paragraph description description, the difficulty based on their developer tools known and the tools of the current project, and estimated time based on their skills. Make sure the project ideas are unique and stand out in a resume as interesting and personalized.'
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

    return ''