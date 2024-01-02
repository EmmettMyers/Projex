import { Project } from '@/types/types';
import axios from 'axios';
import { ref } from 'vue';

export const project_pool = ref<Project[]>([]);

export const preset_project_pool = async () => {
    project_pool.value = []
    const user_data = { email: "emmettleemyers@gmail.com" };
    const saved_response = await axios.post('http://127.0.0.1:8000/get_saved_projects/', user_data);
    const saved_projects = saved_response.data;
    const response = await axios.post('http://127.0.0.1:8000/get_project_pool/', user_data);
    // check if there are any project pool generations
    if (response.data.length > 0){
        const generations = [] as Project[];
        for (const data of response.data){
            // check if generation is in saved projects
            let saved = false;
            for (const project of saved_projects){ 
                if (project['description'] == data['description']){
                    saved = true;
                }
            }
            // push generated project into generations
            const generation: Project = {
                name: data['title'],
                description: data['description'],
                difficulty: data['difficulty'],
                time: data['time'],
                tools: data['tools'],
                saved: saved,
            }
            generations.push(generation);
        }
        project_pool.value = generations;
    }
}