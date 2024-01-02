import { Project } from '@/types/types';
import axios from 'axios';
import { ref } from 'vue';

export const past_generations = ref<Project[]>([]);

export const preset_past_generations = async () => {
    const user_data = { email: localStorage.getItem('userEmail') };
    const saved_response = await axios.post('http://127.0.0.1:8000/get_saved_projects/', user_data);
    const saved_projects = saved_response.data;
    const response = await axios.post('http://127.0.0.1:8000/get_past_generations/', user_data);
    // check if there are any past generations
    if (response.data[1].length > 0){
        const generations = [] as Project[];
        for (const data of response.data[1]){
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
        let randomized_generations = shuffleArray(generations);
        if (randomized_generations.length > 20){
            randomized_generations = randomized_generations.slice(0, 20);
        }
        past_generations.value = randomized_generations;
    }
}

export const shuffleArray = (array: Project[]) => {
    const shuffledArray = [...array];
    shuffledArray.sort(() => Math.random() - 0.5);
    return shuffledArray;
}