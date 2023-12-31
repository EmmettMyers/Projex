<template>
  <div id="prefs" class="center-horiz">
    <div id="top-row">
      <div id="title">{{ title }}</div>
      <div id="addedInfo" v-if="additionalInfo">* {{ additionalInfo }}</div>
      <div v-if="editMode" id="btn-holder">
        <CustomButton
          text="+" 
          backColor="#328D30" 
          textColor="#D8FFD8" 
          horizPad="20px" 
          vertPad="2px" 
          fontSize="20px"
          @click="openAddModal"
        />
      </div>
    </div>
    <div id="box" class="center-vert">
      <div 
        class="option-box center-vert" 
        :class="{ 'delete-border': editMode }"
        v-for="option in options" 
        :key="option"
        @click="deletePreference(option)"
      >
        <div id="option-txt">{{ option }}</div>
        <div v-if="editMode" id="delete-sign">-</div>
      </div>
    </div>
  </div>
</template>
  
<script lang="ts">
  import { defineComponent } from 'vue';
  import CustomButton from './CustomButton.vue';
  import { remove_preference } from '@/utils/preferences';
  
  export default defineComponent({
    name: 'PreferenceBar',
    props: ['title', 'options', 'additionalInfo', 'editMode', 'openModalParent'],
    components: { CustomButton },
    methods: {
      openAddModal() {
        this.openModalParent(this.title);
      },
      deletePreference(option: string) {
        remove_preference(this.title, option);
      }
    },
});
</script>
  
<style lang='scss' scoped>
  #prefs {
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
      #btn-holder {
        margin-left: auto;
        margin-right: 4px;
        padding-top: 3px;
      }
    }
    #box {
      margin-top: 8px;
      width: 88vw;
      height: 80px;
      background: #7DBCCE;
      border-radius: 8px;
      border: 2px solid #313235;
      display: flex;
      padding-left: 20px;
      overflow-x: auto;
      .delete-border {
        -webkit-box-shadow:inset 0px 0px 0px 3px #E22C2C;
        -moz-box-shadow:inset 0px 0px 0px 3px #E22C2C;
        box-shadow:inset 0px 0px 0px 3px #E22C2C;
        transition: background 0.2s ease;
        &:hover {
          cursor: pointer;
          background: #ffc6c6;
        }
      }
      .option-box {
        margin-right: 10px;
        height: 75%;
        padding-left: 40px;
        padding-right: 40px;
        background: white;
        border-radius: 8px;
        position: relative;
        #option-txt {
          font-size: 23px;
          font-weight: 400;
        }
        #delete-sign {
          font-size: 30px;
          font-weight: 400;
          color: #E22C2C;
          position: absolute;
          line-height: 0;
          right: 12px;
          top: 12px;
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
  