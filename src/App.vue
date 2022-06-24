<template>
  <v-app>
    <layout-default>
      <router-view />
    </layout-default>
  </v-app>
</template>

<script lang="ts">
import Vue from "vue";
import LayoutDefault from "./layout/LayoutDefault.vue";
export default Vue.extend({
  name: "App",
  components: {
    LayoutDefault,
  },
  data: () => ({
    //
  }),
  methods: {},
});
</script>

<style>
.v-toolbar__content,
.v-toolbar__extension {
  padding: 0;
}
</style>
