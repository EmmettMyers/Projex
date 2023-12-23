<template>
  <div id="nav" class="center-vert">
    <img id="logo" src="../assets/logos/logo-long3.png" @click="enterHome" />
    <img id="menu" src="../assets/logos/burger-menu2.png" @click="toggleMenu" />
  </div>
  <div style="height: 7vh"></div>
  <MenuModal v-if="menuOpen" />
</template>
  
<script lang="ts">
  import { defineComponent } from 'vue';
  import MenuModal from './MenuModal.vue';
  
  export default defineComponent({
    name: 'NavBar',
    components: { MenuModal },
    data() {
      return {
        menuOpen: false,
      };
    },
    methods: {
      toggleMenu() {
        this.menuOpen = !this.menuOpen;
      },
      enterHome() {
        this.$router.push('/home');
      },
    },
});
</script>
  
<style lang='scss' scoped>
  #nav {
    position: absolute;
    z-index: 10;
    width: 100vw;
    height: 7vh;
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
      z-index: 10;
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
  