<template>
  <div id="header">
    <div id="exit" @click="exitPage">{{ '<' }}</div>
    <div id="title">{{ title }}</div>
    <div id="desc">{{ description }}</div>
  </div>
</template>
  
<script lang="ts">
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'PageHeader',
    props: ['title', 'description', 'miniTitle'],
    methods: {
      exitPage() {
        if (this.title == "Generated Projects"){
          this.$router.go(-2);
        } else if (this.miniTitle){
          this.$router.go(-1);
        } else {
          this.$router.push('/home');
        }
      },
    },
  });
</script>
  
<style lang='scss' scoped>
  #header {
    width: 100vw;
    margin-bottom: 30px;
    #exit {
      font-size: 40px;
      font-weight: 400;
      padding-top: 30px;
      padding-left: 25px;
      line-height: 0;
      transition: color 0.2s ease;
      user-select: none;
      width: 10px;
      &:hover {
        cursor: pointer;
        color: gray;
      }
    }
    #title {
      font-size: 70px;
      font-weight: 700;
      padding-top: 15px;
      padding-left: 75px;
    }
    #desc {
      font-size: 30px;
      font-weight: 400;
      padding-top: 5px;
      padding-left: 75px;
      padding-right: 75px;
    }
  }
</style>
  