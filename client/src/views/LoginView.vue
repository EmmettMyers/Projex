<template>
    <div id="page" v-show="backgroundLoaded">
        <div id="login">
            <div class="center-vert center-horiz">
                <div id="container">
                    <div class="center-horiz">
                        <img id="long-logo" src="../assets/logos/logo-long3.png" />
                        <div id="motto">
                            code your <span>future</span>.
                        </div>
                        <GoogleSignIn />
                    </div>
                </div>
            </div>
        </div>
        <img id="background" src="../assets/logos/coding_w_view.png" />
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import GoogleSignIn from '../components/GoogleSignIn.vue';

export default defineComponent({
    name: 'LoginView',
    components: {
        GoogleSignIn
    },
    data() {
        return {
            backgroundLoaded: false
        };
    },
    mounted() {
        const background = document.getElementById('background');
        if (background) {
            background.addEventListener('load', () => {
                this.backgroundLoaded = true;
            });
        }
    },
});
</script>

<style lang="scss" scoped>
#page {
    background: black;
}
#background {
    width: 100vw;
    height: auto;
    object-fit: cover;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    opacity: .2;
}
#login {
    user-select: none;
    overflow: hidden;
    width: 100vw;
    height: 100vh;
    #container {
        padding-bottom: 8vh;
        #long-logo {
            z-index: 20;
            width: 650px;
        }
        #motto {
            z-index: 20;
            line-height: 0px;
            color: white;
            font-size: 50px;
            font-weight: 400;
            padding-top: 20px;
            span {
                color: #7DBCCE;
            }
        }
    }
}
</style>