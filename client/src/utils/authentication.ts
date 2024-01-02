import { createClient } from '@supabase/supabase-js'
import axios from 'axios';

const supabaseUrl = {URL};
const supabaseKey = {KEY};
const supabase = createClient(supabaseUrl, supabaseKey);

export async function init_google_login() {
    const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'google',
    });
}

export async function logout() {
    supabase.auth.signOut();
    localStorage.setItem('userEmail', '');
}

export async function set_user_email() {
    const user: any = await supabase.auth.getUser();
    if (user.data.user != null){
        const user_email = user.data.user.email;
        localStorage.setItem('userEmail', user_email);
        const user_data = { email: localStorage.getItem('userEmail') };
        const response = await axios.post('http://127.0.0.1:8000/add_new_user/', user_data);
    } else {
        localStorage.setItem('userEmail', '');
    }
}