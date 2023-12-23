<template>
    <div>
        <NavBar />
        <div id="saved">
            <PageHeader :title="pageTitle" :description="pageDescription" />
            <ProjectBox v-for="(project, index) in savedProjects" :key="index" :project="project" />
            <div style="height: 40px"></div>
        </div>
    </div>
</template>
    
<script lang="ts">
    import NavBar from '@/components/NavBar.vue';
    import PageHeader from '@/components/PageHeader.vue';
    import ProjectBox from '@/components/ProjectBox.vue';
    import { savedProjects } from '@/utils/savedProjects';
    import { defineComponent } from 'vue';

    export default defineComponent({
        name: 'SavedView',
        components: { NavBar, PageHeader, ProjectBox },
        data() {
            return {
                pageTitle: "Saved Projects",
                pageDescription: "Stores projects you have saved from generation or community.",
                savedProjects: savedProjects.value
            };
        },
    });
</script>
    
<style lang='scss' scoped>
    #saved {
        height: 93vh;
        overflow-x: hidden;
        overflow-y: auto;
    }
</style>
    