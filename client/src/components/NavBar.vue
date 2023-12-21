<template>
    <div id="nav" class="center-vert">
        <img id="logo" src="../assets/logos/logo-long2.png" />
        <img id="menu" src="../assets/logos/burger-menu2.png" />
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'NavBar',
    methods: {
    }
  });
  </script>
  
  <style lang='scss' scoped>
  #nav {
    width: 100vw;
    height: 60px;
    background: #313235;
    justify-content: space-between;
    #logo {
        height: 40px;
        padding-left: 20px;
        transition: filter 0.3s ease;
        &:hover {
            cursor: pointer;
            filter: brightness(70%);
        }
    }
    #menu {
        height: 25px;
        padding-right: 20px;
        transition: filter 0.3s ease;
        &:hover {
            cursor: pointer;
            filter: brightness(70%);
        }
    }
  }
  </style>
  