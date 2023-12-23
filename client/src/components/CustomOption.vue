<template>
    <div id="add">
        <div id="add-txt">Add your own:</div>
        <input type="text" id="custom-option" v-model="customOptionValue">
        <div id="enter-btn" class="center-vert" @click="createOption">Enter</div>
    </div>
</template>
  
<script lang="ts">
  import { tools, topics } from '@/utils/generateOptions';
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'CustomOption',
    props: ['section', 'addOption'],
    data() {
      return {
        customOptionValue: '',
      };
    },
    methods: {
      createOption() {
        if (this.section == 'Tools'){
          tools.value.unshift(this.customOptionValue);
        } else if (this.section == 'Topics'){
          topics.value.unshift(this.customOptionValue);
        }
        this.addOption(this.customOptionValue);
        this.customOptionValue = '';
      }
    },
  });
</script>
  
<style lang='scss' scoped>
  #add {
    display: flex;
    padding-left: 40px;
    #add-txt { 
        margin-top: 10px;
        font-size: 18px;
        font-weight: 400;
    }
    #custom-option {
        margin-top: 8px;
        margin-left: 8px;
        height: 20px;
        border: 1px solid #C0C0C0;
        border-right: none;
        border-radius: 4px 0px 0px 4px;
        outline: none;
    }
    #enter-btn {
        font-size: 12px;
        font-weight: 500;
        height: 20px;
        margin-top: 8px;
        background: #328D30;
        color: #D8FFD8;
        padding-top: 2px;
        padding-bottom: 2px;
        padding-left: 15px;
        padding-right: 15px;
        border-radius: 0px 4px 4px 0px;
        transition: filter 0.3s ease;
        &:hover {
          cursor: pointer;
          filter: brightness(110%);
        }
    }
  }
</style>
  