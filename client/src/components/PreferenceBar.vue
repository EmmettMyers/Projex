<template>
    <div id="prefs" class="center-horiz">
      <div id="top-row">
        <div id="title">{{ title }}</div>
        <div id="addedInfo" v-if="additionalInfo">* {{ additionalInfo }}</div>
      </div>
      <div id="box" class="center-vert">
        <div class="option-box center-vert" v-for="option in options" :key="option">
          {{ option }}
        </div>
      </div>
    </div>
</template>
  
<script lang="ts">
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'PreferenceBar',
    props: ['title', 'options', 'additionalInfo'],
    methods: {
    },
  });
</script>
  
<style lang='scss' scoped>
  #prefs {
    margin-bottom: 25px;
    #top-row {
      width: 90vw;
      display: flex;
      #title {
        font-size: 30px;
        font-weight: 500;
      }
      #addedInfo {
        padding-top: 13px;
        padding-left: 40px;
        font-size: 16px;
        font-weight: 300;
      }
    }
    #box {
      margin-top: 8px;
      width: 88vw;
      height: 80px;
      background: #7DBCCE;
      border-radius: 8px;
      border: 2px solid #313235;
      display: flex;
      padding-left: 20px;
      overflow-x: auto;
      .option-box {
        margin-right: 10px;
        height: 75%;
        padding-left: 40px;
        padding-right: 40px;
        background: white;
        border-radius: 8px;
        font-size: 23px;
        font-weight: 400;
      }
    }
    #box::-webkit-scrollbar {
      height: 6px;
    }
    #box::-webkit-scrollbar-thumb {
      background-color: #313235;
      transition: background-color 0.3s ease;
    }
    #box::-webkit-scrollbar-thumb:hover {
      background-color: #6e6f73;
    }
    #box::-webkit-scrollbar-track {
      background-color: #7DBCCE;
    }
  }
</style>
  