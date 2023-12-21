import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://hjymcwxdsalayjcsdvkt.supabase.co';
const supabaseKey = {KEY};
const supabase = createClient(supabaseUrl, supabaseKey);

export async function initSupabase() {
    const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'google',
        options: {
            queryParams: {
                access_type: 'offline',
                prompt: 'consent',
            },
        },
    });
    if (error) {
        console.error('Sign-in error:', error);
    } else {
        console.log('Sign-in success. User data:', data);
    }
}