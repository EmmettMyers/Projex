<template>
    <div id="box">

      <div id="top-row" class="center-vert">
        <div id="name">{{ project.name }} &nbsp;<span>|</span></div>
        <div id="tool-holder" v-for="(tool, index) in project.tools" :key="index">
          <img :src="require(`@/assets/tools/${tool.logo}`)" :alt="tool.name" width="30" height="30" />
        </div>
        <div id="btn-holder">
          <CustomButton />
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
    components: { CustomButton },
    data() {
        return {
            project: {
                name: 'Food Cart',
                description: 'A user-friendly web app allowing food cart vendors to showcase their menu, accept orders, and facilitate seamless transactions with customers.',
                difficulty: 'Intermediate',
                time: '2-3 weeks',
                tools: [
                    { name: 'HTML', logo: 'html.png' },
                    { name: 'CSS', logo: 'css.png' },
                    { name: 'JavaScript', logo: 'javascript.png' },
                ],
                image: 'project-image.png',
                saved: false,
            },
        };
    },
    methods: {
    },
  });
  </script>
  
  <style lang='scss' scoped>
  #box {
    background: white;
    border: solid 2px #313235;
    border-radius: 10px;
    width: 100%;
    #top-row {
      display: flex;
      justify-content: flex-start;
      #name {
        font-size: 40px;
        font-weight: 600;
        padding-top: 15px;
        padding-left: 30px;
        padding-right: 15px;
        span {
          color: #7DBCCE;
        }
      }
      #tool-holder {
        padding-top: 25px;
        img {
          padding-left: 5px;
        }
      }
      #btn-holder {
        margin-top: 15px;
        margin-left: auto;
        margin-right: 20px;
      }
    }
    #desc-holder {
      padding-top: 5px;
      padding-bottom: 15px;
      padding-left: 30px;
      padding-right: 30px;
      font-size: 20px;
      font-weight: 400;
      overflow-wrap: break-word;
    }
  }
  </style>
  