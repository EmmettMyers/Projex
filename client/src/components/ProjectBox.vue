<template>
    <div class="center-horiz">
        <div id="box" class="center-vert">
            <div id="content">
                <div id="top-row">
                    <div id="name">{{ project.name }}</div>
                    <div id="divider"></div>
                    <div 
                        id="tool-holder" 
                        v-for="(tool, index) in project.tools" 
                        @mouseover="setTooltip(index)"
                        @mouseout="setTooltip(-1)" :key="index"
                    >
                        <img 
                        :src="require(`@/assets/tools/${tool.toLowerCase()}.png`)" 
                        :alt="tool" 
                        width="35" 
                        height="35"
                        />
                        <div class="tooltip" v-if="tooltipIndex === index">{{ tool }}</div>
                    </div>
                    <div id="divider"></div>
                    <div style="margin-left: 5px;">
                        <div id="difficulty" style="padding-top: 18px;">
                            Relative Difficulty:&nbsp; <span>{{ project.difficulty }}</span>
                        </div>
                        <div id="time">
                            Estimated Time:&nbsp; <span>{{ project.time }}</span>
                        </div>
                    </div>
                    <div id="divider"></div>
                    <div id="code-btn" style="margin-left: 10px;">
                        <CustomButton 
                            text="Starter Code" 
                            backColor="#A9B8BC" 
                            textColor="#313235" 
                            horizPad="30px" 
                            vertPad="8px" 
                            fontSize="18px"
                        />
                    </div>
                    <div id="save-btn" style="margin-left: 5px;">
                        <CustomButton 
                            v-if="project.saved"
                            text="Unsave" 
                            backColor="#E22C2C" 
                            textColor="#FDEBEB" 
                            horizPad="30px" 
                            vertPad="8px" 
                            fontSize="18px"
                            @click="unsaveProject"
                        />
                        <CustomButton 
                            v-else
                            text="Save" 
                            backColor="#328D30" 
                            textColor="#D8FFD8" 
                            horizPad="30px" 
                            vertPad="8px" 
                            fontSize="18px"
                            @click="saveProject"
                        />
                    </div>
                </div>
                <div id="desc-holder">
                    {{ project.description }}
                </div>
            </div>
        </div>
    </div>
</template>
    
<script lang="ts">
    import { defineComponent } from 'vue';
    import CustomButton from '@/components/CustomButton.vue';

    export default defineComponent({
        name: 'ProjectBox',
        components: { CustomButton },
        props: ['project'],
        data() {
            return {
                tooltipIndex: -1
            };
        },
        methods: {
            setTooltip(index: number) {
                this.tooltipIndex = index;
            },
            saveProject() {
                //
            },
            unsaveProject() {
                //
            },
        },
    });
</script>
    
<style lang='scss' scoped>
    .tooltip {
        position: absolute;
        background: #313235;
        color: white;
        padding-top: 5px;
        padding-bottom: 5px;
        padding-left: 10px;
        padding-right: 10px;
        border-radius: 6px;
        font-size: 18px;
    }
    #box {
        background: white;
        border: solid 2px #313235;
        border-radius: 10px;
        width: 90vw;
        height: fit-content;
        margin-bottom: 20px;
        display: flex;
        #content {
            width: 100%;
            #top-row {
                display: flex;
                width: 100%;
                #code-btn, #save-btn {
                    padding-top: 20px;
                }
                #name {
                    max-width: 400px;
                    padding-top: 16px;
                    white-space: nowrap;
                    overflow: hidden;
                    text-overflow: ellipsis; 
                    font-size: 40px;
                    font-weight: 600;
                    padding-left: 36px;
                }
                #divider {
                    width: 4px;
                    height: 40px;
                    background: #7DBCCE;
                    margin-top: 20px;
                    margin-left: 30px;
                    margin-right: 20px;
                    border-radius: 4px;
                }
                #tool-holder {
                    padding-top: 22px;
                    img {
                        padding-left: 8px;
                    }
                }
                #btn-holder {
                    margin-top: 12px;
                    margin-left: auto;
                    margin-right: 20px;
                }
                #difficulty, #time {
                    font-size: 18px;
                    line-height: 22px;
                    font-weight: 500;
                    span {
                        font-size: 18px;
                        font-weight: 700;
                    }
                }
            }
            #desc-holder {
                width: 95%;
                padding-top: 10px;
                padding-bottom: 25px;
                padding-left: 36px;
                font-size: 20px;
                font-weight: 400;
                overflow-wrap: break-word;
            }
        }
    }
</style>
    