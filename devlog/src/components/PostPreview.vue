<template>
  <div class="post-preview">
    <v-card
      style="border-top-right-radius: 20px; border-top-left-radius: 20px"
      color="#ffffff00"
      elevation="0"
      dark
    >
      <div class="post-img">
        <v-img
          @click="openPost"
          :src="post.image"
          :aspect-ratio="16 / 9"
          max-height="250"
        ></v-img>
      </div>
      <v-card-title @click="openPost" class="post-preview-title">{{
        post.title
      }}</v-card-title>
      <v-card-subtitle style="color: #565f89">{{
        post.timestamp
      }}</v-card-subtitle>
      <v-chip-group style="padding-left: 16px; padding-right: 16px" column>
        <v-chip v-for="tag in post.tags" :key="tag" color="#bb9af7" outlined>{{
          tag
        }}</v-chip>
      </v-chip-group>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "PostPreview",
  props: ["post", "file"],
  methods: {
    openPost() {
      this.$router.push({ name: "Post", params: { postName: this.file } });
    },
  },
};
</script>

<style>
.post-preview {
  max-width: 800px;
  padding-top: 20px;
  padding-bottom: 10px;
  padding-left: 20px;
  padding-right: 20px;
  border-radius: 40px;
  background: #1a1b26;
  box-shadow: 14px 14px 29px #13131b, -14px -14px 29px #212331;
}

.post-preview .post-img {
  transition: all 0.1s ease-in-out;
  cursor: pointer;
  overflow: hidden;
  border: solid 5px #1a1b26;
  border-radius: 20px;
  margin-top: 5px;
  margin-left: 5px;
  margin-right: 5px;
  box-shadow: 5px 5px 10px #13131b, -5px -5px 10px #212331;
}
.post-preview .post-img:hover {
  transition: all 0.1s ease-in-out;
  box-shadow: 30px 30px 60px #13141c, -30px -30px 60px #212230;
}

.post-preview-title {
  cursor: pointer;
  color: #c0caf5;
}
.post-preview-title:hover {
  color: #7aa2f7;
  text-decoration: underline;
}
</style>
