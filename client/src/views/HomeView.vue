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
        <div v-if="loading == true" id="loader-holder" class="center-horiz">
          <div id="loader"></div>
        </div>
        <div v-if="loading == false" id="project-holder">
          <HomeProjectBox v-for="(project, index) in pastGeneratedProjects" :key="index" :project="project" />
          <div style="height: 30px"></div>
        </div>
      </div>

      <div id="right-holder">
        <div id="pref-btn" class="center-horiz center-vert" @click="navigate('preferences')">
          Set Project Preferences
        </div>
        <div id="gen-btn" class="center-horiz center-vert" @click="navigate('generate')">
          Generate<br>Project<br>Ideas
        </div>
        <div id="bottom-btn-holder">
          <div id="saved-btn" class="center-horiz center-vert" @click="navigate('saved')">
            View<br>Saved<br>Projects
          </div>
          <div id="pool-btn" class="center-horiz center-vert" @click="navigate('pool')">
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
  import { past_generations, preset_past_generations } from '@/utils/pastGenerations';
  import { defineComponent } from 'vue';

  export default defineComponent({
    name: 'HomeView',
    components: { NavBar, HomeProjectBox },
    methods: {
      navigate(page: string) {
        this.$router.push(page);
      },
    },
    data() {
      return {
        pastGeneratedProjects: past_generations,
        loading: true
      };
    },
    async mounted() {
      await preset_past_generations();
      this.loading = false;
    }
  });
</script>

<style lang='scss' scoped>
  #home {
    user-select: none;
    display: flex;
    justify-content: center;
    #left-holder {
      margin-right: 2vw;
      margin-top: 6vh;
      width: 40vw;
      #motto {
        font-size: 3.75vw;
        font-weight: 700;
        line-height: 110%;
        span {
          font-weight: 900;
        }
      }
      #blue-line {
        width: 96%;
        margin-top: 2px;
        height: 7px;
        background: #7DBCCE;
        border-radius: 4px;
      }
      #past-generations-title {
        position: absolute;
        bottom: 60vh;
        font-size: 30px;
        font-weight: 500;
      }
      #loader-holder {
        #loader {
          width: 80px;
          aspect-ratio: 1;
          border-radius: 50%;
          border: 14px solid #7DBCCE;
          border-right-color: #313235;
          animation: l2 .75s infinite linear;
          margin-top: 28vh;
        }
        @keyframes l2 {to{transform: rotate(1turn)}}
      }
      #project-holder {
        height: 58vh;
        width: 40vw;
        overflow-x: hidden;
        overflow-y: auto;
        position: absolute;
        bottom: 0px;
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
      margin-left: 2vw;
      margin-top: 7vh;
      width: 40vw;
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
        height: 14vh;
        font-size: 2vw;
      }
      #gen-btn {
        margin-top: 10px;
        height: 38vh;
        font-size: 3.1vw;
      }
      #bottom-btn-holder {
        display: flex;
        justify-content: space-between;
        margin-top: 10px;
        #saved-btn, #pool-btn {
          height: 24vh;
          font-size: 2vw;
          width: 49.15%;
        }
      }
    }
  }
</style>
