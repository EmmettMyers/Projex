import { ref } from 'vue';
import { Options, Project } from '../types/types';
import axios from 'axios';

export const generated_projects = ref<Project[]>([]);

export const selected_options: Options = {
    'type': ref<string[]>([]),
    'difficulty': ref<string[]>([]),
    'time': ref<string[]>([]),
    'tools': ref<string[]>([]),
    'topics': ref<string[]>([]),
}

export const get_project_generations = async () => {
    const parsable_options = {
        type: [...selected_options.type.value],
        difficulty: [...selected_options.difficulty.value],
        time: [...selected_options.time.value],
        tools: [...selected_options.tools.value],
        topics: [...selected_options.topics.value],
    }
    const user_data = { 
        email: "emmettleemyers@gmail.com",
        options: parsable_options,
    };
    const response = await axios.post('http://127.0.0.1:8000/get_project_generations/', user_data);
    for (const data of response.data){
        const generation: Project = {
            name: data['Title'],
            description: data['Description'],
            difficulty: data['Difficulty'],
            time: data['Time'],
            tools: data['Coding Tools'],
            saved: false,
        }
        generated_projects.value.push(generation);
    }
}

export const reset_selected_options = () => {
    Object.keys(selected_options).forEach((key) => {
        selected_options[key].value = [];
    });
}

export const add_option = (section: string, option: string) => {
    section = section.toLowerCase();
    const sectionRef = selected_options[section as keyof typeof selected_options];
    if (!sectionRef.value.includes(option)){
        sectionRef.value.push(option);
    }
}

export const remove_option = (section: string, option: string) => {
    section = section.toLowerCase();
    var option_index = selected_options[section as keyof typeof selected_options].value.indexOf(option);
    selected_options[section as keyof typeof selected_options].value.splice(option_index, 1);
}