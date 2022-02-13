<template>
  <div class="post-page">
    <div style="height: 10px"></div>
    <div v-html="markdownToHtml"></div>
    <div style="height: 30px"></div>
  </div>
</template>

<script>
import { marked } from "marked";
import highlight from "highlight.js";
import "highlight.js/styles/shades-of-purple.css";

export default {
  name: "Post",
  data: () => ({
    postName: undefined,
    markdownSource: undefined,
  }),
  created() {
    this.postName = this.$route.params.postName;
    const markdownSource = require(`@/posts/${this.$route.params.postName}`);
    this.markdownSource = markdownSource.default;
  },
  computed: {
    markdownToHtml() {
      return marked(this.markdownSource, {
        renderer: new marked.Renderer(),
        highlight: function (code, lang) {
          const language = highlight.getLanguage(lang) ? lang : "plaintext";
          return highlight.highlight(code, { language }).value;
        },
        langPrefix: "hljs language-", // highlight.js css expects a top-level 'hljs' class.
        pedantic: false,
        gfm: true,
        breaks: false,
        sanitize: false,
        smartLists: true,
        smartypants: false,
        xhtml: false,
      });
    },
  },
};
</script>

<style>
.post-page {
  width: 90%;
  margin-left: auto;
  margin-right: auto;
}

.post-page h1 {
  font-size: 40px;
}

.post-page blockquote {
  width: 90%;
  font-size: 17px;
  padding-left: 10px;
  padding-top: 10px;
  padding-right: 10px;
  padding-bottom: 1px;
  background-color: #24283b;
  border-top-right-radius: 20px;
  border-bottom-right-radius: 20px;
  border-left: 5px solid #565f89;
  box-shadow: 5px 5px 10px #13131b, -5px -5px 10px #212331;
}

.post-page .hljs-number {
  color: #ff9e64;
}
.post-page .hljs-keyword {
  color: #bb9af7;
}
.post-page pre {
  font-size: 17px;
  background-color: #24283b;
  border-radius: 20px;
  color: #7aa2f7;
  margin-top: 20px;
  margin-bottom: 20px;
  overflow: hidden;
  border: solid 2px #414868;
  box-shadow: 5px 5px 10px #13131b, -5px -5px 10px #212331;
}

.post-page img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  margin-top: 20px;
  margin-bottom: 20px;
  width: 95%;
  max-width: 800px;
  transition: all 0.1s ease-in-out;
  border: solid 5px #1a1b26;
  border-radius: 20px;
  box-shadow: 5px 5px 10px #13131b, -5px -5px 10px #212331;
}
.post-page img:hover {
  transition: all 0.1s ease-in-out;
  box-shadow: 30px 30px 60px #13141c, -30px -30px 60px #212230;
}
</style>
