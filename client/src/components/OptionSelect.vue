<template>
    <div 
      id="options" 
      :class="{ 'center-horiz': true, 
                'vert-scroll': vertScroll, 
                'modal-view': inModal
              }"
    >
      <div id="top-row" v-if="!inModal">
        <div id="title">{{ title }}</div>
        <div id="addedInfo" v-if="additionalInfo">* {{ additionalInfo }}</div>
        <CustomOption v-if="custom" :section="title" :addOption="addOption" />
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
  import { add_option, remove_option } from '@/utils/generatedProjects';
  import { formatToCamelCase, preferences } from '@/utils/preferences';
  import { types, difficulties, times, tools, topics, reset_tools, reset_topics }  from '@/utils/generateOptions';
  
  export default defineComponent({
    name: 'OptionSelect',
    props: ['title', 'additionalInfo', 'custom', 'vertScroll', 'inModal', 'parentSelectedSet'],
    components: { CustomOption },
    data() {
      return {
        selectedOptions: [] as string[],
        options: [] as string[]
      };
    },
    methods: {
      addOption(option: string){
        this.selectedOptions.unshift(option);
        if (this.inModal === undefined) {
          add_option(this.title, option);
        }
      },
      optionClicked(option: string) {
        // change local selectedOptions
        const index = this.selectedOptions.indexOf(option);
        if (index === -1) {
          this.selectedOptions.push(option);
          // in generate page
          if (this.inModal === undefined) {
            add_option(this.title, option);
          }
        } else {
          this.selectedOptions.splice(index, 1);
          // in generate page
          if (this.inModal === undefined) {
            remove_option(this.title, option);
          }
        }
        // set global selectedOptions if in preferences
        if (this.parentSelectedSet) {
          this.parentSelectedSet(this.selectedOptions);
        }
      },
      setOptions() {
        if (this.inModal){
          switch (this.title) {
            case "Project Interests":
              this.options = (types.value ?? []); break;
            case "Tools Known":
              this.options = (tools.value ?? []); break;
            case "Tools Desired To Learn":
              this.options = (tools.value ?? []); break;
            case "Topic Interests":
              this.options = (topics.value ?? []); break;
          }
        } else {
          switch (this.title) {
            case "Type":
              this.options = (types.value ?? []); break;
            case "Difficulty":
              this.options = (difficulties.value ?? []); break;
            case "Time":
              this.options = (times.value ?? []); break;
            case "Tools":
              this.options = (tools.value ?? []); break;
            case "Topics":
              this.options = (topics.value ?? []); break;
          }
        }
      },
      removeExistingPreferencesFromOptions(){
        const parsable_title: string = formatToCamelCase(this.title);
        const section_preferences: string[] = preferences[parsable_title as keyof typeof preferences].value;
        this.options = this.options.filter((item: string) => !section_preferences.includes(item));
      }
    },
    mounted() {
      this.selectedOptions = []
      reset_tools();
      reset_topics();
      this.setOptions();
      if (this.inModal){
        this.removeExistingPreferencesFromOptions();
      }
    }
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
  .modal-view {
    #top-row {
      width: 64vw !important;
    }
    #box {
      width: 62vw !important;
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
  