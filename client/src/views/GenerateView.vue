<template>
    <div>
        <NavBar />
        <div id="generate">
            <PageHeader :title="pageTitle" :description="pageDescription" />
            <OptionSelect title="Type" :options="types" vert-scroll="true" />
            <OptionSelect title="Difficulty" :options="difficulties" additionalInfo="aggregate based on your developer proficiencies" />
            <OptionSelect title="Time" :options="times" />
            <OptionSelect title="Tools" :options="tools" custom="true" vert-scroll="true" />
            <OptionSelect title="Topics" :options="topics" custom="true" vert-scroll="true" />
            <div id="btn-layer">
                <div id="btn-holder">
                    <CustomButton 
                        text="Generate" 
                        backColor="#328D30" 
                        textColor="#D8FFD8" 
                        horizPad="80px" 
                        vertPad="12px" 
                        fontSize="30px"
                        @click="generateProjects"
                    />
                </div>
            </div>
            <div style="height: 40px"></div>
        </div>
    </div>
</template>
    
<script lang="ts">
    import NavBar from '@/components/NavBar.vue';
    import CustomButton from '@/components/CustomButton.vue';
    import OptionSelect from '@/components/OptionSelect.vue';
    import PageHeader from '@/components/PageHeader.vue';
    import { types, difficulties, times, tools, topics, reset_tools, reset_topics }  from '@/utils/generateOptions';
    import { defineComponent } from 'vue';
    import { get_project_generations, reset_selected_options } from '@/utils/generatedProjects';

    export default defineComponent({
        name: 'GenerateView',
        components: { NavBar, PageHeader, OptionSelect, CustomButton },
        data() {
            return {
                pageTitle: "Generate Project Ideas",
                pageDescription: "Our artificial intelligence tools will create project ideas based on your preferences and options chosen below.",
                types: types,
                difficulties: difficulties,
                times: times,
                tools: tools,
                topics: topics
            };
        },
        methods: {
            async generateProjects() {
                this.$router.push('/loading');
                await get_project_generations();
                this.$router.push('/generated');
            },
        },
        mounted() {
            reset_selected_options();
            reset_tools();
            reset_topics();
        }
    });
</script>
    
<style lang='scss' scoped>
    #generate {
        height: 93vh;
        overflow-x: hidden;
        overflow-y: auto;
        #btn-layer {
            display: flex;
            justify-content: center;
            #btn-holder {
                display: flex;
                justify-content: end;
                padding-top: 20px;
                padding-bottom: 50px;
                width: 90vw;
            }
        }
    }
</style>
    