<template>
    <div id="menu">
        <div @click="navigate('generate')">generate</div>
        <div @click="navigate('pool')">project pool</div>
        <div @click="navigate('saved')">saved</div>
        <div @click="navigate('preferences')">preferences</div>
        <div @click="logout()">log out</div>
    </div>
</template>
    
<script lang="ts">
    import { logout } from '@/utils/authentication';
    import { defineComponent } from 'vue';
    
    export default defineComponent({
        name: 'MenuModal',
        methods: {
            navigate(page: string) {
                this.$router.push(page);
            },
            async logout() {
                await logout();
                this.navigate('login');
            }
        },
    });
</script>
    
<style lang='scss' scoped>
    #menu {
        z-index: 5;
        height: 156px;
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
    