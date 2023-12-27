<template>
  <div 
    id="button"
    :style="{ 
      backgroundColor: backColor, 
      color: textColor, 
      paddingLeft: horizPad, 
      paddingRight: horizPad,
      paddingTop: vertPad,
      paddingBottom: vertPad,
      fontSize: fontSize
    }"
  >
    {{ text }}
  </div>
</template>
  
<script lang="ts">
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'CustomButton',
    props: ['text', 'backColor', 'textColor', 'horizPad', 'vertPad', 'fontSize'],
    methods: {
    },
  });
</script>
  
<style lang='scss' scoped>
  #button {
    user-select: none;
    border-radius: 6px;
    font-weight: 500;
    transition: filter 0.2s ease;
    &:hover {
      cursor: pointer;
      filter: brightness(110%);
    }
  }
</style>
  