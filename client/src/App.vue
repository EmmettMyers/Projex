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
  ::-webkit-scrollbar {
    width: 6px;
  }
  ::-webkit-scrollbar-thumb {
    background-color: #313235;
    transition: background-color 0.3s ease;
  }
  ::-webkit-scrollbar-thumb:hover {
    background-color: #6e6f73;
  }
  ::-webkit-scrollbar-track {
    background-color: #7DBCCE;
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
