<template>
  <div class="devlog-header">
    <h1 id="github-link" @click="openGithub">Gregory Kogan's</h1>
    <h2>⌨️ Devlog</h2>
  </div>
</template>

<script>
export default {
  name: "DevlogHeader",
  methods: {
    openGithub() {
      window.open("https://github.com/GregoryKogan", "_blank").focus();
    },
  },
};
</script>

<style>
.devlog-header {
  margin-top: 10px;
  margin-bottom: 20px;
}

.devlog-header #github-link {
  cursor: pointer;
  color: #c0caf5;
}
.devlog-header #github-link:hover {
  color: #7aa2f7;
  text-decoration: underline;
}
</style>
