<template>
    <div>
        <NavBar />
        <div id="pool">
            <PageHeader :title="pageTitle" :description="pageDescription" />
            <div v-if="loading == true" id="loader-holder" class="center-horiz">
                <div id="loader"></div>
            </div>
            <ProjectBox 
                v-if="loading == false" 
                v-for="(project, index) in projectPool" 
                :key="index" 
                :project="project" 
            />
            <div style="height: 40px"></div>
        </div>
    </div>
</template>
    
<script lang="ts">
    import NavBar from '@/components/NavBar.vue';
    import PageHeader from '@/components/PageHeader.vue';
    import ProjectBox from '@/components/ProjectBox.vue';
    import { preset_project_pool, project_pool } from '@/utils/projectPool';
    import { defineComponent } from 'vue';

    export default defineComponent({
        name: 'PoolView',
        components: { NavBar, PageHeader, ProjectBox },
        data() {
            return {
                pageTitle: "Project Pool",
                pageDescription: "Discover unsaved projects generated from other users and their preferences.",
                projectPool: project_pool,
                loading: true
            };
        },
        async mounted() {
            await preset_project_pool();
            this.loading = false;
        }
    });
</script>
    
<style lang='scss' scoped>
    #pool {
        height: 93vh;
        overflow-x: hidden;
        overflow-y: auto;
        #loader-holder {
            #loader {
                width: 80px;
                aspect-ratio: 1;
                border-radius: 50%;
                border: 14px solid #7DBCCE;
                border-right-color: #313235;
                animation: l2 .75s infinite linear;
                margin-top: 20vh;
            }
            @keyframes l2 {to{transform: rotate(1turn)}}
        }
    }
</style>
    