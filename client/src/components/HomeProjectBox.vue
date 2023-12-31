<template>
  <div id="box">

    <div id="top-row" class="center-vert">
      <div class="center-vert">
        <div id="name">{{ project.name }}</div>
        <div id="divider"></div>
      </div>
      <div 
        id="tool-holder" 
        v-for="(tool, index) in project.tools" 
        @mouseover="setTooltip(index)"
        @mouseout="setTooltip(-1)" :key="index"
      >
        <img 
          :src="require(`@/assets/tools/${tool.toLowerCase()}.png`)" 
          :alt="tool" 
          width="25" 
          height="25"
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
          vertPad="8px" 
          fontSize="18px"
        />
        <CustomButton 
          v-else
          text="Save" 
          backColor="#328D30" 
          textColor="#D8FFD8" 
          horizPad="30px" 
          vertPad="8px" 
          fontSize="18px"
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
  
  export default defineComponent({
    name: 'HomeProjectBox',
    props: ['project'],
    components: { CustomButton },
    data() {
      return {
        tooltipIndex: -1
      };
    },
    methods: {
      setTooltip(index: number) {
        this.tooltipIndex = index;
      }
    }
  });
</script>
  
<style lang='scss' scoped>
  .tooltip {
    position: absolute;
    background: #313235;
    color: white;
    padding-top: 5px;
    padding-bottom: 5px;
    padding-left: 10px;
    padding-right: 10px;
    border-radius: 6px;
    font-size: 15px;
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
      #name {
        max-width: 360px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis; 
        padding-top: 12px;
        font-size: 30px;
        font-weight: 600;
        padding-left: 20px;
      }
      #divider {
        width: 4px;
        height: 30px;
        background: #7DBCCE;
        margin-top: 10px;
        margin-left: 20px;
        margin-right: 16px;
        border-radius: 4px;
      }
      #tool-holder {
        padding-top: 16px;
        img {
          padding-left: 5px;
        }
      }
      #btn-holder {
        margin-top: 12px;
        margin-left: auto;
        margin-right: 20px;
      }
    }
    #desc-holder {
      padding-top: 5px;
      padding-bottom: 15px;
      padding-left: 20px;
      padding-right: 20px;
      font-size: 20px;
      font-weight: 400;
      overflow-wrap: break-word;
    }
  }
</style>
  