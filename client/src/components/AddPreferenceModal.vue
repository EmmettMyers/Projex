<template>
    <div @click="closeModal" id="modal-holder" class="center-horiz center-vert">
        <div @click.stop id="modal">
            <div @click="closeModal" id="exit">x</div>
            <div id="title">Add Preferences <span> - {{ title }}</span></div>
            <OptionSelect 
                :title="title"
                vertScroll="true" 
                inModal="true" 
                :parentSelectedSet="setSelectedOption"
            />
            <div id="btn-layer">
                <div id="btn-holder">
                    <CustomButton 
                        text="Save" 
                        backColor="#328D30" 
                        textColor="#D8FFD8" 
                        horizPad="60px" 
                        vertPad="8px" 
                        fontSize="25px"
                        @click="addPreferences"
                    />
                </div>
            </div>
        </div>
    </div>
    <div id="shadow"></div>
</template>
    
<script lang="ts">
    import { defineComponent } from 'vue';
    import OptionSelect from './OptionSelect.vue';
    import { reset_tools, reset_topics }  from '@/utils/generateOptions';
    import CustomButton from './CustomButton.vue';
    import { add_preference } from '@/utils/preferences';

    export default defineComponent({
        name: 'AddPreferenceModal',
        props: ['title', 'closeModal'],
        components: { CustomButton, OptionSelect },
        data() {
            return {
                selectedOptions: ['']
            };
        },
        methods: {
            setSelectedOption(selectedOptions: string[]) {
                this.selectedOptions = selectedOptions;
            },
            addPreferences() {
                for (const preference of this.selectedOptions){
                    add_preference(this.title, preference);
                }
                this.closeModal();
            }
        },
        mounted() {
            reset_tools();
            reset_topics();
        },
    });
</script>
    
<style lang='scss' scoped>
    #modal-holder {
        position: absolute;
        width: 100vw;
        height: 100vh;
        z-index: 70;
        #modal {
            width: 70vw;
            padding-bottom: 40px;
            border-radius: 10px;
            background: #F0F1F4;
            z-index: 70;
            position: absolute;
            #exit {
                position: absolute;
                top: 8px;
                right: 28px;
                font-size: 40px;
                font-weight: 300;
                user-select: none;
                transition: color 0.2s ease;
                &:hover {
                    cursor: pointer;
                    color: gray;
                }
            }
            #title {
                font-size: 50px;
                font-weight: 700;
                padding-top: 30px;
                padding-bottom: 20px;
                padding-left: 45px;
                span {
                    font-size: 35px;
                    font-weight: 400;
                }
            }
            #btn-layer {
                display: flex;
                justify-content: center;
                #btn-holder {
                    display: flex;
                    justify-content: end;
                    padding-top: 6px;
                    width: 64vw;
                }
            }
        }
    }
    #shadow {
        height: 100vh;
        width: 100vw;
        position: absolute;
        z-index: 50;
        background: black;
        opacity: .8;
    }
</style>
    