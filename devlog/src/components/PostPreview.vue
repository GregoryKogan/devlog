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
          :src="post.image"
          :aspect-ratio="16 / 9"
          max-height="250"
        ></v-img>
      </div>
      <v-card-title style="color: #c0caf5">{{ post.title }}</v-card-title>
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
  props: ["post"],
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

.post-img {
  overflow: hidden;
  border: solid 5px #1a1b26;
  border-radius: 20px;
  margin-top: 5px;
  margin-left: 5px;
  margin-right: 5px;
  box-shadow: 5px 5px 10px #13131b, -5px -5px 10px #212331;
}
</style>
