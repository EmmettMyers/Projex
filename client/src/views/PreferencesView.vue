<template>
  <div>
    <NavBar />
    <div id="preferences">
      <PageHeader :title="pageTitle" :description="pageDescription" />
      <PreferenceBar title="Project Interests" :options="projectInterests" />
      <PreferenceBar title="Tools Known" :options="toolsKnown" />
      <PreferenceBar title="Tools Desired To Learn" :options="toolsDesiredToLearn" />
      <PreferenceBar title="Topic Interests" :options="topicInterests" />
      <div style="height: 40px"></div>
    </div>
  </div>
</template>
  
<script lang="ts">
  import NavBar from '@/components/NavBar.vue';
  import PageHeader from '@/components/PageHeader.vue';
  import PreferenceBar from '@/components/PreferenceBar.vue';
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'PreferencesView',
    components: { NavBar, PageHeader, PreferenceBar },
    data() {
      return {
        pageTitle: "Preferences",
        pageDescription: "Stores your generation preferences to streamline the creation process.",
        projectInterests: ['Website', 'Machine Learning', 'Mobile App'],
        toolsKnown: ['HTML', 'CSS', 'Java', 'Python', 'JavaScript'],
        toolsDesiredToLearn: ['React', 'Vue', 'Flask'],
        topicInterests: ['Sports', 'Video Games', 'Cats'],
      };
    },
  });
</script>
  
<style lang='scss' scoped>
  #preferences {
    height: 93vh;
    overflow-x: hidden;
    overflow-y: scroll;
  }
</style>
  