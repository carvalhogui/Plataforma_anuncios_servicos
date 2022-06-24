<template>
  <div>
    <DialogAnuncio v-model="dialogAnuncio" />
    <v-app>
      <v-app-bar
        clipped-left
        app
        dark
        height="100x"
        color="white"
        extension-height="150"
      >
        <v-container background-color="white">
          <v-row align="center" class="ml-4 mr-4">
            <v-col cols="11">
              <h2 style="color: #1c4163">ServiConnect</h2>
            </v-col>
            <v-col cols="1">
              <v-btn
                dark
                height="52px"
                color="#1C4163"
                class="ml-15"
                @click="dialogAnuncio = true"
              >
                Anunciar</v-btn
              >
            </v-col>
          </v-row>
        </v-container>
        <template #extension>
          <v-toolbar color="#1C4163" height="150px">
            <v-row align="center" class="ml-4 mr-4">
              <v-col cols="3">
                <router-link
                  :to="{ name: 'Home' }"
                  class="text-decoration-none white--text"
                >
                  <v-toolbar-title>
                    <h2>Encontre o profissional</h2>
                    <h2>que precisa em instantes!</h2>
                  </v-toolbar-title>
                </router-link>
              </v-col>
              <v-col cols="8">
                <v-text-field
                  placeholder="Busque por nome,categoria,cidade...."
                  outlined
                  background-color="white"
                  color="black"
                  hide-details
                  light
                  clearable
                  v-model="search"
                >
                </v-text-field>
              </v-col>
              <v-col cols="1">
                <v-btn light height="52px">
                  <h4 style="color: #1c4163">Pesquisar</h4>
                </v-btn>
              </v-col>
            </v-row>
          </v-toolbar>
        </template>
      </v-app-bar>

      <TheNavDrawer />

      <v-main>
        <v-container>
          <slot></slot>
        </v-container>
      </v-main>

      <v-footer app class="justify-center"> <i>ServiConnect</i></v-footer>
    </v-app>
  </div>
</template>

<script lang="ts">
import DialogAnuncio from "@/components/DialogAnuncio.vue";
import Vue from "vue";
import TheNavDrawer from "../components/TheNavDrawer.vue";
export default Vue.extend({
  components: { TheNavDrawer, DialogAnuncio },
  name: "LayoutDefault",

  data: () => ({
    search: null,
    dialogAnuncio: false,
  }),
});
</script>
