<template>
    <div id="prefs" class="center-horiz">
      <div id="title">{{ title }}</div>
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
    props: ['title', 'options'],
    methods: {
    },
  });
</script>
  
<style lang='scss' scoped>
  #prefs {
    margin-bottom: 25px;
    #title {
      width: 90vw;
      font-size: 30px;
      font-weight: 500;
    }
    #box {
      margin-top: 8px;
      width: 89vw;
      height: 80px;
      background: #7DBCCE;
      border-radius: 8px;
      border: 2px solid #313235;
      display: flex;
      padding-left: 10px;
      .option-box {
        margin-left: 10px;
        height: 75%;
        padding-left: 40px;
        padding-right: 40px;
        background: white;
        border-radius: 8px;
        font-size: 23px;
        font-weight: 400;
      }
    }
  }
</style>
  