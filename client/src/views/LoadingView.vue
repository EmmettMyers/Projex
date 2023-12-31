<template>
    <div>
        <NavBar />
        <div id="loading" class="center-horiz center-vert">
            <div id="text">{{ text }}</div>
            <div id="loader"></div>
        </div>
    </div>
</template>
    
<script lang="ts">
    import NavBar from '@/components/NavBar.vue';
    import { defineComponent } from 'vue';

    export default defineComponent({
        name: 'LoadingView',
        props: ['text'],
        components: { NavBar },
        data() {
            return {
            };
        },
    });
</script>
    
<style lang='scss' scoped>
    #loading {
        height: 93vh;
        overflow-x: hidden;
        overflow-y: auto;
        #text {
            font-size: 40px;
            font-weight: 500;
            padding-bottom: 40px;
        }
        /* HTML: <div class="loader"></div> */
        #loader {
            width: 120px;
            aspect-ratio: 1;
            border-radius: 50%;
            border: 20px solid #7DBCCE;
            border-right-color: #313235;
            animation: l2 1.5s infinite linear;
            margin-bottom: 80px;
        }
        @keyframes l2 {to{transform: rotate(1turn)}}

    }
</style>
    