<template>
  <div>
    <v-navigation-drawer
      app
      absolute
      hide-overlay
      permanent
      clipped
      width="350px"
    >
      <div class="d-flex justify-center"><h1>Categorias</h1></div>
    </v-navigation-drawer>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "TheNavDrawer",
  data: () => ({}),
});
</script>
