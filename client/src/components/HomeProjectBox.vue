<template>
  <div id="box">

    <div id="top-row" class="center-vert">
      <div class="center-vert">
        <div 
          id="name-holder"
          @mouseover="setTooltip(-1)"
          @mouseout="setTooltip(-2)" 
        >
          <div id="name">{{ project.name }}</div>
          <div class="tooltip" v-if="tooltipIndex === -1">{{ project.name }}</div>
        </div>
        <div id="divider"></div>
      </div>
      <div 
        id="tool-holder" 
        v-for="(tool, index) in project.tools.slice(0, 4)" 
        @mouseover="setTooltip(index)"
        @mouseout="setTooltip(-2)" 
        :key="index"
      >
        <img 
          :src="getToolImageSrc(tool)" 
          :alt="tool" 
          style="height: 25px; width: auto;"
        />
        <div class="tooltip" v-if="tooltipIndex === index">{{ tool }}</div>
      </div>
      <div id="btn-holder">
        <CustomButton 
          v-if="project.saved"
          text="Unsave" 
          backColor="#E22C2C" 
          textColor="#FDEBEB" 
          horizPad="30px" 
          vertPad="6px" 
          fontSize="18px"
          @click="unsaveProject"
        />
        <CustomButton 
          v-else
          text="Save" 
          backColor="#328D30" 
          textColor="#D8FFD8" 
          horizPad="30px" 
          vertPad="6px" 
          fontSize="18px"
          @click="saveProject"
        />
      </div>
    </div>

    <div id="desc-holder">
      {{ project.description }}
    </div>
    
  </div>
</template>
  
<script lang="ts">
  import { defineComponent } from 'vue';
  import CustomButton from '@/components/CustomButton.vue';
  import { save_project, unsave_project } from '@/utils/savedProjects';
  
  export default defineComponent({
    name: 'HomeProjectBox',
    props: ['project'],
    components: { CustomButton },
    data() {
      return {
        tooltipIndex: -2
      };
    },
    methods: {
      setTooltip(index: number) {
        this.tooltipIndex = index;
      },
      getToolImageSrc(tool: string) {
        try {
          if (tool == 'Next.js'){
            tool = 'Next'
          }
          return require(`@/assets/tools/${tool.toLowerCase()}.png`);
        } catch (error) {
          return require(`@/assets/tools/unknown.png`);
        }
      },
      saveProject() {
        save_project(this.project.name, this.project.description);
        this.project.saved = true;
      },
      unsaveProject() {
        unsave_project(this.project.name, this.project.description);
        this.project.saved = false;
      },  
    }
  });
</script>
  
<style lang='scss' scoped>
  .tooltip {
    position: absolute;
    background: #313235;
    color: white;
    top: 48px;
    padding-top: 5px;
    padding-bottom: 5px;
    padding-left: 10px;
    padding-right: 10px;
    border-radius: 6px;
    font-size: 18px;
    z-index: 60;
  }
  #box {
    background: white;
    border: solid 2px #313235;
    border-radius: 10px;
    width: 97%;
    margin-bottom: 15px;
    #top-row {
      display: flex;
      justify-content: flex-start;
      #name-holder {
        position: relative;
        padding-left: 20px;
        #name {
          max-width: 320px;
          white-space: nowrap;
          overflow: hidden;
          text-overflow: ellipsis; 
          padding-top: 12px;
          font-size: 30px;
          font-weight: 600;
        }
        .tooltip {
          margin-top: 4px;
        }
      }
      #divider {
        width: 4px;
        height: 30px;
        background: #7DBCCE;
        margin-top: 10px;
        margin-left: 14px;
        margin-right: 12px;
        border-radius: 4px;
      }
      #tool-holder {
        position: relative;
        padding-top: 16px;
        img {
          padding-left: 5px;
        }
      }
      #btn-holder {
        padding-left: 16px;
        margin-top: 8px;
        margin-left: auto;
        margin-right: 20px;
      }
    }
    #desc-holder {
      padding-top: 5px;
      padding-bottom: 18px;
      padding-left: 20px;
      padding-right: 20px;
      font-size: 20px;
      font-weight: 400;
      overflow-wrap: break-word;
    }
  }
</style>
  