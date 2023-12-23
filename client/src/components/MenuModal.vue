<template>
    <div id="menu">
        <div @click="enterGenerate">generate</div>
        <div @click="enterPool">project pool</div>
        <div @click="enterSaved">saved</div>
        <div @click="enterPreferences">preferences</div>
        <div @click="logOut">log out</div>
    </div>
</template>
    
<script lang="ts">
    import { defineComponent } from 'vue';
    
    export default defineComponent({
        name: 'MenuModal',
        methods: {
            enterGenerate() {
                this.$router.push('/generate');
            },
            enterPool() {
                this.$router.push('/pool');
            },
            enterSaved() {
                this.$router.push('/saved');
            },
            enterPreferences() {
                this.$router.push('/preferences');
            },
            logOut() {
                this.$router.push('/login');
            },
        },
    });
</script>
    
<style lang='scss' scoped>
    #menu {
        z-index: 5;
        height: 160px;
        width: 130px;
        position: absolute;
        right: 0;
        top: 7vh;
        background: #313235;
        color: white;
        border-radius: 0px 0px 0px 12px;
        box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.7);
        padding-top: 10px;
        div {
            user-select: none;
            z-index: 6;
            font-size: 16px;
            text-align: center;
            margin-bottom: 10px;
            transition: color 0.2s ease;
            &:hover {
                cursor: pointer;
                color: #7DBCCE;
            }
        }
    }
</style>
    