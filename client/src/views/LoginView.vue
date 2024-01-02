<template>
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
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import GoogleSignIn from '../components/GoogleSignIn.vue';
import { set_user_email } from '@/utils/authentication';

export default defineComponent({
    name: 'LoginView',
    components: {
        GoogleSignIn
    },
});
</script>

<style lang="scss" scoped>
#login {
    user-select: none;
    overflow: hidden;
    width: 100vw;
    height: 100vh;
    background: #313235;
    #container {
        padding-bottom: 8vh;
        #long-logo {
            width: 650px;
        }
        #motto {
            line-height: 0px;
            color: white;
            font-size: 50px;
            font-weight: 400;
            padding-top: 30px;
            span {
                color: #7DBCCE;
            }
        }
    }
}
</style>