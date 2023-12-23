<template>
    <div>
        <NavBar />
        <div id="generated">
            <PageHeader :title="pageTitle" :description="pageDescription" />
            <ProjectBox v-for="(project, index) in generatedProjects" :key="index" :project="project" />
            <div style="height: 40px"></div>
        </div>
    </div>
</template>
    
<script lang="ts">
    import NavBar from '@/components/NavBar.vue';
    import PageHeader from '@/components/PageHeader.vue';
    import ProjectBox from '@/components/ProjectBox.vue';
    import { generatedProjects } from '@/utils/generatedProjects';
    import { defineComponent } from 'vue';

    export default defineComponent({
        name: 'PoolView',
        components: { NavBar, PageHeader, ProjectBox },
        data() {
            return {
                pageTitle: "Generated Projects",
                pageDescription: "Based on the parameters selected and user data.",
                generatedProjects: generatedProjects
            };
        },
    });
</script>
    
<style lang='scss' scoped>
    #generated {
        height: 93vh;
        overflow-x: hidden;
        overflow-y: auto;
    }
</style>