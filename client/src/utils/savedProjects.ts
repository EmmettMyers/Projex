import { Project } from '@/types/types';
import axios from 'axios';
import { ref } from 'vue';

export const saved_projects = ref<Project[]>([]);

export const preset_saved_projects = async () => {
    saved_projects.value = []
    const user_data = { email: "emmettleemyers@gmail.com" };
    const response = await axios.post('http://127.0.0.1:8000/get_saved_projects/', user_data);
    // check if there are any saved projects
    if (response.data.length > 0){
        for (const data of response.data){
            const saved_project: Project = {
                name: data['title'],
                description: data['description'],
                difficulty: data['difficulty'],
                time: data['time'],
                tools: data['tools'],
                saved: true,
            }
            saved_projects.value.push(saved_project);
        }
    }
}

export const save_project = async (title: string, description: string) => {
    const project_data = { 
        email: "emmettleemyers@gmail.com",
        title: title,
        description: description
    };
    const response = await axios.post('http://127.0.0.1:8000/add_saved_project/', project_data);
}

export const unsave_project = async (title: string, description: string) => {
    const project_data = { 
        email: "emmettleemyers@gmail.com",
        title: title,
        description: description
    };
    const response = await axios.post('http://127.0.0.1:8000/delete_saved_project/', project_data);
}