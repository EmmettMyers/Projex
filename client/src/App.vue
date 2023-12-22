<template>
  <router-view/>
</template>

<style lang="scss">
body {
  padding: 0; 
  margin: 0;
  font-family: 'Roboto';
  background: #F0F1F4;
  color: #313235;
  overflow: hidden;
}
.center-horiz {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}
.center-vert {
  display: flex;
  align-items: center;
  height: 100%;
}
</style>
