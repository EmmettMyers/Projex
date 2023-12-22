<template>
    <div class="center-horiz">
        <div id="box" class="center-vert">
            <div id="content">
                <div id="top-row">
                    <div id="name">{{ project.name }}</div>
                    <div id="divider"></div>
                    <div id="tool-holder" v-for="(tool, index) in project.tools" :key="index">
                        <img 
                            :src="require(`@/assets/tools/${tool.logo}`)" 
                            :alt="tool.name" 
                            width="35" 
                            height="35" 
                        />
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
                            text="Unsave" 
                            backColor="#E22C2C" 
                            textColor="#FDEBEB" 
                            horizPad="30px" 
                            vertPad="8px" 
                            fontSize="18px"
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
        data() {
            return {
                project: {
                    name: 'SportsMatch Tracker',
                    description: 'Create a dynamic sports match tracker website that allows users to input and track scores, statistics, and highlights of their favorite sports matches. Users can customize the interface based on their preferred sports, teams, and players. Implement machine learning algorithms to provide insightful match predictions and player performance analytics. The website can also feature real-time updates and notifications for ongoing matches, making it an engaging platform for sports enthusiasts.',
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
    