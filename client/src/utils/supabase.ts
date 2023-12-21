import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://hjymcwxdsalayjcsdvkt.supabase.co';
const supabaseKey = 'KEY';
const supabase = createClient(supabaseUrl, supabaseKey);

export async function initGooglePopup() {
    const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'google',
    });
    if (error) {
        console.error('Sign-in error:', error);
    } else {
        console.log('Sign-in success. User data:', data);
    }
}

async function handleSignInWithGoogle(response: any) {
    alert(response.credential);
    /*const { data, error } = await supabase.auth.signInWithIdToken({
        provider: 'google',
        token: response.credential,
        nonce: 'NONCE', // must be the same one as provided in data-nonce (if any)
    })*/
}