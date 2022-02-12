<template>
  <div class="home-page">
    <h1 style="margin-bottom: 20px; margin-top: 10px">Devlog</h1>
    <div v-for="data in postsData" :key="data.timestamp">
      <PostPreview :post="data" style="margin-left: auto; margin-right: auto" />
      <div style="height: 50px"></div>
    </div>
  </div>
</template>

<script>
import postsDataJson from "@/postsData.json";
import PostPreview from "@/components/PostPreview.vue";

export default {
  name: "Home",
  components: { PostPreview },
  data: () => ({
    postsData: postsDataJson,
  }),
};
</script>

<style>
.home-page {
  width: 90%;
  margin-left: auto;
  margin-right: auto;
}
</style>
