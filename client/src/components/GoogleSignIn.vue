<template>
  <div id="button">
    <div class="center-vert" @click="signIn">
      <img src="../assets/logos/google.png" />
      <div id="signin-txt">Sign in with Google</div>
    </div>
  </div>
</template>

<script lang="ts">
  import { initGooglePopup } from '@/utils/supabase';
  import axios from 'axios';
  import { defineComponent } from 'vue';

  export default defineComponent({
    name: 'GoogleSignIn',
    methods: {
      async signIn() {
        //initGooglePopup();
        const user_data = {
          email: "emmettleemyers@gmail.com",
          first_name: "Emmett",
          last_name: "Myers",
        };
        const response = await axios.post('http://127.0.0.1:8000/add_new_user/', user_data);
        this.$router.push('/home');
      }
    }
  });
</script>

<style lang='scss' scoped>
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
