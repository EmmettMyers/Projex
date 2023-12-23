<template>
    <div id="options" :class="{ 'center-horiz': true, 'vert-scroll': vertScroll }">
      <div id="top-row">
        <div id="title">{{ title }}</div>
        <div id="addedInfo" v-if="additionalInfo">* {{ additionalInfo }}</div>
        <CustomOption v-if="custom" :section="title" :selectedOptions="selectedOptions" />
      </div>
      <div id="box" class="center-vert">
        <div 
          class="option-box center-vert" 
          v-for="option in options" 
          :key="option"
          @click="optionClicked(option)"
          :class="{ 'clicked': selectedOptions.includes(option) }"
        >
          {{ option }}
        </div>
      </div>
    </div>
</template>
  
<script lang="ts">
  import { defineComponent } from 'vue';
  import CustomOption from './CustomOption.vue';
  
  export default defineComponent({
    name: 'OptionSelect',
    props: ['title', 'options', 'additionalInfo', 'custom', 'vertScroll'],
    components: { CustomOption },
    data() {
      return {
        selectedOptions: [] as string[],
      };
    },
    methods: {
      optionClicked(option: string) {
        const index = this.selectedOptions.indexOf(option);
        if (index === -1) {
          this.selectedOptions.push(option);
        } else {
          this.selectedOptions.splice(index, 1);
        }
      },
    },
});
</script>
  
<style lang='scss' scoped>
  .vert-scroll {
    #box {
      flex-wrap: wrap;
      height: auto !important;
      max-height: 400px !important;
      overflow-y: auto;
      padding-top: 10px !important;
      .option-box {
        margin-bottom: 10px !important;
      }
    }
  }
  #options {
    margin-bottom: 25px;
    #top-row {
      width: 90vw;
      display: flex;
      #title {
        font-size: 30px;
        font-weight: 500;
      }
      #addedInfo {
        padding-top: 13px;
        padding-left: 40px;
        font-size: 16px;
        font-weight: 300;
      }
    }
    #box {
      user-select: none;
      margin-top: 8px;
      width: 88vw;
      height: 75px;
      background: #7DBCCE;
      border-radius: 8px;
      border: 2px solid #313235;
      display: flex;
      padding-left: 20px;
      overflow-x: auto;
      .clicked {
        background: yellow !important;
      }
      .option-box {
        white-space: nowrap;
        margin-right: 10px;
        height: 50px;
        padding-left: 40px;
        padding-right: 40px;
        background: white;
        border-radius: 8px;
        font-size: 20px;
        font-weight: 400;
        transition: background 0.2s ease;
        &:hover {
          cursor: pointer;
          background: yellow !important;
        }
      }
    }
    #box::-webkit-scrollbar {
      height: 6px;
    }
    #box::-webkit-scrollbar-thumb {
      background-color: #313235;
      transition: background-color 0.3s ease;
    }
    #box::-webkit-scrollbar-thumb:hover {
      background-color: #6e6f73;
    }
    #box::-webkit-scrollbar-track {
      background-color: #7DBCCE;
    }
  }
</style>
  