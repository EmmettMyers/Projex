<template>
  <div>
    <NavBar />
    <div id="preferences">
      <PageHeader :title="pageTitle" :description="pageDescription" />
      <PreferenceBar title="Project Interests" :options="projectInterests" />
      <PreferenceBar title="Tools Known" :options="toolsKnown" />
      <PreferenceBar title="Tools Desired To Learn" :options="toolsDesiredToLearn" />
      <PreferenceBar title="Topic Interests" :options="topicInterests" />
      <div style="height: 60px"></div>
    </div>
  </div>
</template>
  
<script lang="ts">
  import NavBar from '@/components/NavBar.vue';
  import PageHeader from '@/components/PageHeader.vue';
  import PreferenceBar from '@/components/PreferenceBar.vue';
  import { projectInterests, toolsKnown, toolsDesiredToLearn, topicInterests }  from '@/utils/preferences';
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'PreferencesView',
    components: { NavBar, PageHeader, PreferenceBar },
    data() {
      return {
        pageTitle: "Preferences",
        pageDescription: "Stores your generation preferences to streamline the creation process.",
        projectInterests: projectInterests.value,
        toolsKnown: toolsKnown.value,
        toolsDesiredToLearn: toolsDesiredToLearn.value,
        topicInterests: topicInterests.value,
      };
    },
  });
</script>
  
<style lang='scss' scoped>
  #preferences {
    height: 93vh;
    overflow-x: hidden;
    overflow-y: auto;
  }
</style>
  