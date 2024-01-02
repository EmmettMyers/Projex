<template>
</template>
    
<script lang="ts">
    import { set_user_email } from '@/utils/authentication';
    import { defineComponent } from 'vue';

    export default defineComponent({
        name: 'AuthView',
        async mounted() {
            await set_user_email();
            if (localStorage.getItem('userEmail') == ''){
                this.$router.push('/login');
            } else {
                this.$router.push('/home');
            }
        },
    });
</script>
    