<template>
  <div>
    <NavBar />
    <div id="preferences">
      <div id="button-holder">
        <CustomButton
          text="Edit" 
          backColor="#7DBCCE" 
          textColor="#313235" 
          horizPad="50px" 
          vertPad="12px" 
          fontSize="25px"
        />
      </div>
      <PageHeader :title="pageTitle" :description="pageDescription" />
      <PreferenceBar title="Project Interests" :options="projectInterests" />
      <PreferenceBar title="Tools Known" :options="toolsKnown" additionalInfo="B: beginner, I: intermediate, A: advanced" />
      <PreferenceBar title="Tools Desired To Learn" :options="toolsDesiredToLearn" />
      <PreferenceBar title="Topic Interests" :options="topicInterests" />
      <div style="height: 60px"></div>
    </div>
  </div>
</template>
  
<script lang="ts">
  import CustomButton from '@/components/CustomButton.vue';
  import NavBar from '@/components/NavBar.vue';
  import PageHeader from '@/components/PageHeader.vue';
  import PreferenceBar from '@/components/PreferenceBar.vue';
  import { projectInterests, toolsKnown, toolsDesiredToLearn, topicInterests }  from '@/utils/preferences';
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'PreferencesView',
    components: { NavBar, PageHeader, PreferenceBar, CustomButton },
    data() {
      return {
        pageTitle: "Preferences",
        pageDescription: "Stores your generation preferences to streamline the creation process.",
        projectInterests: projectInterests,
        toolsKnown: toolsKnown,
        toolsDesiredToLearn: toolsDesiredToLearn,
        topicInterests: topicInterests,
      };
    },
  });
</script>
  
<style lang='scss' scoped>
  #preferences {
    height: 93vh;
    overflow-x: hidden;
    overflow-y: auto;
    #button-holder {
      display: flex;
      float: right;
      margin-top: 75px;
      margin-right: 5vw;
    }
  }
</style>
  