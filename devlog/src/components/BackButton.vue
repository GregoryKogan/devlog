<template>
  <v-btn @click="goBack" elevation="10" large color="#bb9af7" rounded outlined>
    <v-icon left> mdi-arrow-left </v-icon>
    Back
  </v-btn>
</template>

<script>
export default {
  name: "BackButton",
  methods: {
    goBack() {
      this.$router.push("/");
    },
  },
};
</script>
