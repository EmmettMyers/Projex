<template>
    <div>
        <NavBar />
        <div id="generate">
            <PageHeader :title="pageTitle" :description="pageDescription" />
            <div style="height: 40px"></div>
        </div>
    </div>
</template>
    
<script lang="ts">
    import NavBar from '@/components/NavBar.vue';
    import PageHeader from '@/components/PageHeader.vue';
    import { defineComponent } from 'vue';

    export default defineComponent({
        name: 'GenerateView',
        components: { NavBar, PageHeader },
        data() {
            return {
                pageTitle: "Generate Project Ideas",
                pageDescription: "Our artificial intelligence tools will create project ideas based on your preferences and options chosen below.",
            };
        },
    });
</script>
    
<style lang='scss' scoped>
    #generate {
        height: 93vh;
        overflow-x: hidden;
        overflow-y: auto;
    }
</style>
    