<template>
    <div>
        <NavBar />
        <div id="pool">
            <PageHeader :title="pageTitle" :description="pageDescription" />
            <ProjectBox v-for="(project, index) in projectPool" :key="index" :project="project" />
            <div style="height: 40px"></div>
        </div>
    </div>
</template>
    
<script lang="ts">
    import NavBar from '@/components/NavBar.vue';
    import PageHeader from '@/components/PageHeader.vue';
    import ProjectBox from '@/components/ProjectBox.vue';
    import { projectPool } from '@/utils/project-pool';
    import { defineComponent } from 'vue';

    export default defineComponent({
        name: 'PoolView',
        components: { NavBar, PageHeader, ProjectBox },
        data() {
            return {
                pageTitle: "Project Pool",
                pageDescription: "Discover unsaved projects generated from other users and their preferences.",
                projectPool: projectPool.value
            };
        },
    });
</script>
    
<style lang='scss' scoped>
    #pool {
        height: 93vh;
        overflow-x: hidden;
        overflow-y: auto;
    }
</style>
    