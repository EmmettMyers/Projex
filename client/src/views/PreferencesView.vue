<template>
  <AddPreferenceModal 
    v-if="modalOpen" 
    :title="modalTitle"
    :closeModal="closeAddModal"
  />
  <div>
    <NavBar />
    <div id="preferences">
      <div id="button-holder">
        <CustomButton
          v-if="editMode"
          @click="savePreferences"
          text="Save" 
          backColor="#328D30" 
          textColor="#D8FFD8" 
          horizPad="50px" 
          vertPad="12px" 
          fontSize="25px"
          style="margin-right: 6px;"
        />
        <CustomButton
          v-if="editMode"
          @click="cancelChanges"
          text="Cancel" 
          backColor="#E22C2C" 
          textColor="#FDEBEB" 
          horizPad="35px" 
          vertPad="12px" 
          fontSize="25px"
        />
        <CustomButton
          v-else
          @click="toggleEditMode"
          text="Edit" 
          backColor="#7DBCCE" 
          textColor="#313235" 
          horizPad="50px" 
          vertPad="12px" 
          fontSize="25px"
        />
      </div>
      <PageHeader :title="pageTitle" :description="pageDescription" />
      <div v-if="loading == true" id="loader-holder" class="center-horiz">
        <div id="loader"></div>
      </div>
      <PreferenceBar 
        v-if="loading == false"
        title="Project Interests" 
        :options="preferences.projectInterests" 
        :editMode="editMode" 
        :openModalParent="openAddModal"
      />
      <PreferenceBar 
        v-if="loading == false"
        title="Tools Known" 
        :options="preferences.toolsKnown" 
        :editMode="editMode" 
        additionalInfo="B: beginner, I: intermediate, A: advanced" 
        :openModalParent="openAddModal"
      />
      <PreferenceBar 
        v-if="loading == false"
        title="Tools Desired To Learn" 
        :editMode="editMode" 
        :options="preferences.toolsDesiredToLearn"
        :openModalParent="openAddModal"
      />
      <PreferenceBar 
        v-if="loading == false"
        title="Topic Interests" 
        :editMode="editMode" 
        :options="preferences.topicInterests" 
        :openModalParent="openAddModal"
      />
      <div style="height: 60px"></div>
    </div>
  </div>
</template>
  
<script lang="ts">
  import AddPreferenceModal from '@/components/AddPreferenceModal.vue';
  import CustomButton from '@/components/CustomButton.vue';
  import NavBar from '@/components/NavBar.vue';
  import PageHeader from '@/components/PageHeader.vue';
  import PreferenceBar from '@/components/PreferenceBar.vue';
  import { cancel_preferences_changes, preferences, preset_preferences, save_preferences_changes }  from '@/utils/preferences';
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'PreferencesView',
    components: { NavBar, PageHeader, PreferenceBar, CustomButton, AddPreferenceModal },
    data() {
      return {
        pageTitle: "Preferences",
        pageDescription: "Stores your generation preferences to streamline the creation process.",
        editMode: false,
        preferences: preferences,
        modalOpen: false,
        modalTitle: "",
        loading: true
      };
    },
    methods: {
      openAddModal(title: string) {
        this.modalOpen = true;
        this.modalTitle = title;
      },
      closeAddModal() {
        this.modalOpen = false;
      },
      toggleEditMode() {
        this.editMode = !this.editMode;
      },
      cancelChanges() {
        cancel_preferences_changes();
        this.toggleEditMode();
      },
      savePreferences() {
        save_preferences_changes();
        this.toggleEditMode();
      }
    },
    async mounted() {
      await preset_preferences();
      this.loading = false;
    }
  });
</script>
  
<style lang='scss' scoped>
  #preferences {
    height: 93vh;
    overflow-x: hidden;
    overflow-y: auto;
    #button-holder {
      display: flex;
      float: right;
      margin-top: 65px;
      margin-right: 5vw;
    }
    #loader-holder {
      #loader {
        width: 80px;
        aspect-ratio: 1;
        border-radius: 50%;
        border: 14px solid #7DBCCE;
        border-right-color: #313235;
        animation: l2 .75s infinite linear;
        margin-top: 20vh;
      }
      @keyframes l2 {to{transform: rotate(1turn)}}
    }
  }
</style>
  