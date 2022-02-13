<template>
  <div class="post-page">
    <h1>Hello World!</h1>
    <h2>{{ postName }}</h2>
    <!-- <div v-html="markdownToHtml"></div> -->
    <markdownSource />
  </div>
</template>

<script>
import { marked } from 'marked';
import markdownSource from "@/posts/InitialCommit.md";

export default {
  name: "Post",
  components: {markdownSource},
  data: () => ({
    postName: undefined,
  }),
  created() {
    this.postName = this.$route.params.postName;
  },
  computed: {
   markdownToHtml(){
     return marked(this.markdownSource);
   }
 }
};
</script>

<style></style>
