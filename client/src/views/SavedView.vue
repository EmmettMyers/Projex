<template>
    <div>
        <NavBar />
        <div id="saved">
            <PageHeader :title="pageTitle" :description="pageDescription" />
            <div v-if="loading == true" id="loader-holder" class="center-horiz">
                <div id="loader"></div>
            </div>
            <ProjectBox 
                v-if="loading == false" 
                v-for="(project, index) in savedProjects" 
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
    import { preset_saved_projects, saved_projects } from '@/utils/savedProjects';
    import { defineComponent } from 'vue';

    export default defineComponent({
        name: 'SavedView',
        components: { NavBar, PageHeader, ProjectBox },
        data() {
            return {
                pageTitle: "Saved Projects",
                pageDescription: "Stores projects you have saved from generation or community.",
                savedProjects: saved_projects,
                loading: true
            };
        },
        async mounted() {
            await preset_saved_projects();
            this.loading = false;
        }
    });
</script>
    
<style lang='scss' scoped>
    #saved {
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
    