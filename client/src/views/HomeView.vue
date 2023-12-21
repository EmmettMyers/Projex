<template>
  <div>
    <NavBar />
    <div id="home">

      <div id="left-holder">
        <div id="motto">
          Use <span>AI</span> to create coding personal project ideas.
        </div>
        <div id="blue-line"></div>
        <div id="past-generations-title">Your Past Generated Projects</div>
        <HomeProjectBox />
      </div>

      <div id="right-holder">
      </div>

    </div>
  </div>
</template>

<script lang="ts">
import NavBar from '@/components/NavBar.vue';
import HomeProjectBox from '@/components/HomeProjectBox.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'HomeView',
    components: { NavBar, HomeProjectBox }
});
</script>

<style lang='scss' scoped>
#home {
  user-select: none;
  display: flex;
  justify-content: center;
  #left-holder {
    margin-top: 50px;
    width: 630px;
    #motto {
      font-size: 60px;
      font-weight: 700;
      line-height: 110%;
      span {
        font-weight: 900;
      }
    }
    #blue-line {
      width: 615px;
      margin-top: 2px;
      height: 7px;
      background: #7DBCCE;
      border-radius: 4px;
    }
    #past-generations-title {
      margin-top: 50px;
      font-size: 30px;
      font-weight: 500;
      padding-bottom: 15px;
    }
  }
}
</style>
