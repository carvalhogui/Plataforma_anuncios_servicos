/* eslint-disable vue/multi-word-component-names */
<template>
  <div>
    <div class="d-flex justify-center mb-4">
      <h1>Últimos anúncios</h1>
    </div>
    <v-card max-width="375" class="mx-auto" elevation="2">
      <v-card-title>
        <div class="text-h5 pl-1">Flavio Vicentini</div>
      </v-card-title>
      <v-card-subtitle class="mb-0 pb-0">
        <div class="pl-1">Engenharia</div>
      </v-card-subtitle>
      <v-divider class="mx-4"></v-divider>
      <v-card-text class="mt-0 pt-0">
        <v-card-subtitle class="font-weight-bold pb-1 pl-0"
          >Serviços de engenharia</v-card-subtitle
        >
        ldkiushalduhsadluoashlduiahsiduahsodiahsduihsaiudhoijshnljkhdlkjshdjklshjkldhslkjdhslkjdhskjldh
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Corrupti solu
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias, at
        veniam. Molestiae quia animi eaque, maiores eos nesciunt dicta cumque!
        Vero dolores veritatis itaque quae repudiandae provident consequuntur
        libero pariatur.
      </v-card-text>
      <v-list>
        <v-list-item>
          <v-list-item-icon>
            <v-icon color="indigo"> mdi-phone </v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>(650) 555-1234</v-list-item-title>
          </v-list-item-content>

          <v-list-item-icon>
            <v-icon>mdi-message-text</v-icon>
          </v-list-item-icon>
        </v-list-item>

        <v-divider inset></v-divider>

        <v-list-item>
          <v-list-item-icon>
            <v-icon color="indigo"> mdi-email </v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>aliconnors@example.com</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-divider inset></v-divider>

        <v-list-item>
          <v-list-item-icon>
            <v-icon color="indigo"> mdi-map-marker </v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>1400 Main Street</v-list-item-title>
            <v-list-item-subtitle>Orlando, FL 79938</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-list-item class="d-flex justify-center">
          <v-list-item-icon>
            <v-icon color="indigo" class="mr-4"> mdi-facebook </v-icon>
            <v-icon color="indigo" class="mr-4"> mdi-instagram </v-icon>
            <v-icon color="indigo" class="mr-4"> mdi-linkedin </v-icon>
          </v-list-item-icon>
        </v-list-item>
      </v-list>
    </v-card>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "Home",
  data: () => ({}),
});
</script>
