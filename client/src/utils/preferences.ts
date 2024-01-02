import { Preferences } from '@/types/types';
import axios from 'axios';
import { ref } from 'vue';

export const preferences: Preferences = {
    'projectInterests': ref<string[]>([]),
    'toolsKnown': ref<string[]>([]),
    'toolsDesiredToLearn': ref<string[]>([]),
    'topicInterests': ref<string[]>([]),
}

let past_preferences = {
    'projectInterests': [] as string[],
    'toolsKnown': [] as string[],
    'toolsDesiredToLearn': [] as string[],
    'topicInterests': [] as string[],
};

export const preset_preferences = async () => {
    const user_data = { email: "emmettleemyers@gmail.com" };
    const response = await axios.post('http://127.0.0.1:8000/get_preferences/', user_data);
    if (response.data[1].length > 0){
        const data = response.data[1][0];
        // set current preferences
        preferences.projectInterests.value = data['project_interests'];
        preferences.toolsKnown.value = data['tools_known'];
        preferences.toolsDesiredToLearn.value = data['tools_desired_to_learn'];
        preferences.topicInterests.value = data['topic_interests'];
        // set past preferences (deep copy)
        past_preferences = {
            projectInterests: [...preferences.projectInterests.value],
            toolsKnown: [...preferences.toolsKnown.value],
            toolsDesiredToLearn: [...preferences.toolsDesiredToLearn.value],
            topicInterests: [...preferences.topicInterests.value],
        }
    } 
}

export const add_preference = (section: string, preference: string) => {
    section = formatToCamelCase(section);
    const sectionRef = preferences[section as keyof typeof preferences];
    if (!sectionRef.value.includes(preference)){
        sectionRef.value.push(preference);
    }
}

export const remove_preference = (section: string, preference: string) => {
    section = formatToCamelCase(section);
    var preference_index = preferences[section as keyof typeof preferences].value.indexOf(preference);
    preferences[section as keyof typeof preferences].value.splice(preference_index, 1);
}

export const save_preferences_changes = async () => {
    const user_data = { 
        email: "emmettleemyers@gmail.com",
        projectInterests: [...preferences.projectInterests.value],
        toolsKnown: [...preferences.toolsKnown.value],
        toolsDesiredToLearn: [...preferences.toolsDesiredToLearn.value],
        topicInterests: [...preferences.topicInterests.value],
    };
    const response = await axios.post('http://127.0.0.1:8000/update_preferences/', user_data);
    if (response.data[1].length > 0){
        const data = response.data[1][0];
        // set current preferences
        preferences.projectInterests.value = data['project_interests'];
        preferences.toolsKnown.value = data['tools_known'];
        preferences.toolsDesiredToLearn.value = data['tools_desired_to_learn'];
        preferences.topicInterests.value = data['topic_interests'];
        // set past preferences (deep copy)
        past_preferences = {
            projectInterests: [...preferences.projectInterests.value],
            toolsKnown: [...preferences.toolsKnown.value],
            toolsDesiredToLearn: [...preferences.toolsDesiredToLearn.value],
            topicInterests: [...preferences.topicInterests.value],
        }
    }
}

export const cancel_preferences_changes = () => {
    preferences.projectInterests.value = past_preferences.projectInterests;
    preferences.toolsKnown.value = past_preferences.toolsKnown;
    preferences.toolsDesiredToLearn.value = past_preferences.toolsDesiredToLearn;
    preferences.topicInterests.value = past_preferences.topicInterests;
}

const formatToCamelCase = (input: string): string =>
  input
    .split(' ')
    .map((word, index) => (index === 0 ? word.toLowerCase() : word.charAt(0).toUpperCase() + word.slice(1)))
    .join('');