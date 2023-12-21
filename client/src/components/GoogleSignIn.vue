<template>
  <div id="button">
    <div class="center-vert">
      <img src="../assets/google.png" />
      <div id="signin-txt">Sign in with Google</div>
    </div>
    <div></div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'GoogleSignIn'
});
</script>

<style scoped>
#button {
  width: 450px;
  height: 70px;
  margin-top: 60px;
  border-radius: 9px;
  background: linear-gradient(to right, #ffffff 50%, #9ed5e4 50%);
  background-size: 200% 100%;
  transition: background-position 0.5s ease;
  &:hover {
    cursor: pointer;
    background-position: -100% 0;
  }
  img {
    width: 45px;
    margin-left: 20px;
  }
  #signin-txt {
    font-size: 26px;
    font-weight: 600;
    width: 100%;
    padding-right: 30px;
    text-align: center;
  }
}
</style>
