<template>
  <div id="box">

    <div id="top-row" class="center-vert">
      <div class="center-vert">
        <div id="name">{{ project.name }}</div>
        <div id="divider">&nbsp; | </div>
      </div>
      <div id="tool-holder" v-for="(tool, index) in project.tools" :key="index">
        <img :src="require(`@/assets/tools/${tool.logo}`)" :alt="tool.name" width="25" height="25" />
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
        padding-top: 10px;
        font-size: 30px;
        font-weight: 600;
        color: #7DBCCE;
        padding-right: 10px;
      }
      #tool-holder {
        padding-top: 20px;
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
      padding-bottom: 20px;
      padding-left: 20px;
      padding-right: 20px;
      font-size: 20px;
      font-weight: 400;
      overflow-wrap: break-word;
    }
  }
</style>
  