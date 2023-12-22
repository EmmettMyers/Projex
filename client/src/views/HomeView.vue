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
        <div id="project-holder">
          <HomeProjectBox v-for="(project, index) in pastGeneratedProjects" :key="index" :project="project" />
          <div style="height: 30px"></div>
        </div>
      </div>

      <div id="right-holder">
        <div id="pref-btn" class="center-horiz center-vert" @click="enterPreferences">
          Set Project Preferences
        </div>
        <div id="gen-btn" class="center-horiz center-vert" @click="enterGenerate">
          Generate<br>Project<br>Ideas
        </div>
        <div id="bottom-btn-holder">
          <div id="saved-btn" class="center-horiz center-vert" @click="enterSaved">
            View<br>Saved<br>Projects
          </div>
          <div id="pool-btn" class="center-horiz center-vert" @click="enterPool">
            Explore<br>Project<br>Pool
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script lang="ts">
  import NavBar from '@/components/NavBar.vue';
  import HomeProjectBox from '@/components/HomeProjectBox.vue';
  import { pastGenerations } from '@/utils/past-generations';
  import { defineComponent } from 'vue';

  export default defineComponent({
    name: 'HomeView',
    components: { NavBar, HomeProjectBox },
    methods: {
      enterPreferences() {
        this.$router.push('/preferences');
      },
      enterSaved() {
        this.$router.push('/saved');
      },
      enterPool() {
        this.$router.push('/pool');
      },
      enterGenerate() {
        this.$router.push('/generate');
      },
    },
    data() {
      return {
        pastGeneratedProjects: pastGenerations.value
      };
    },
  });
</script>

<style lang='scss' scoped>
  #home {
    user-select: none;
    display: flex;
    justify-content: center;
    #left-holder {
      margin-right: 40px;
      margin-top: 50px;
      width: 670px;
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
      #project-holder {
        height: 440px;
        overflow-x: hidden;
        overflow-y: auto;
      }
      #project-holder::-webkit-scrollbar {
        width: 6px;
      }
      #project-holder::-webkit-scrollbar-thumb {
        background-color: #313235;
        transition: background-color 0.3s ease;
      }
      #project-holder::-webkit-scrollbar-thumb:hover {
        background-color: #6e6f73;
      }
      #project-holder::-webkit-scrollbar-track {
        background-color: #7DBCCE;
      }
    }
    #right-holder {
      margin-left: 50px;
      margin-top: 50px;
      width: 620px;
      #pref-btn, #gen-btn, #saved-btn, #pool-btn {
        background: #7DBCCE;
        border-radius: 10px;
        font-weight: 600;
        text-align: center;
        transition: filter 0.3s ease;
        &:hover {
          cursor: pointer;
          filter: brightness(110%);
        }
      }
      #pref-btn {
        height: 100px;
        font-size: 30px;
      }
      #gen-btn {
        margin-top: 10px;
        height: 300px;
        font-size: 48px;
      }
      #bottom-btn-holder {
        display: flex;
        justify-content: space-between;
        margin-top: 10px;
        #saved-btn, #pool-btn {
          height: 200px;
          font-size: 30px;
          width: 305px;
        }
      }
    }
  }
</style>
