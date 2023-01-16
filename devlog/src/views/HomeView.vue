<template>
  <div class="home-page">
    <devlog-header />
    <div v-for="key in Object.keys(postsData)" :key="key">
      <post-preview
        :post="postsData[key]"
        :file="key"
        style="margin-left: auto; margin-right: auto"
      />
      <div style="height: 50px"></div>
    </div>
  </div>
</template>

<script>
import postsDataJson from "@/postsData.json";
import PostPreview from "@/components/PostPreview.vue";
import DevlogHeader from "@/components/DevlogHeader.vue";

export default {
  name: "HomeView",
  components: { PostPreview, DevlogHeader },
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
