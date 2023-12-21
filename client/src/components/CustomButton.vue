<template>
    <div id="button">
      {{ text }}
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'CustomButton',
    data() {
        return {
            text: 'Save',
        };
    },
    methods: {
    },
  });
  </script>
  
  <style lang='scss' scoped>
  #button {
    background: #328D30;
    border-radius: 4px;
    color: #D8FFD8;
    font-size: 17px;
    font-weight: 500;
    padding-top: 8px;
    padding-bottom: 8px;
    padding-left: 22px;
    padding-right: 22px;
    transition: filter 0.3s ease;
    &:hover {
      cursor: pointer;
      filter: brightness(120%);
    }
  }
  </style>
  