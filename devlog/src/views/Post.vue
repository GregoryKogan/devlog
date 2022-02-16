<template>
  <div class="post-page">
    <div style="height: 10px"></div>
    <div v-html="markdownToHtml"></div>
    <div style="height: 30px"></div>
    <BackButton />
    <div style="height: 30px"></div>
  </div>
</template>

<script>
import BackButton from "@/components/BackButton.vue";
import { marked } from "marked";
import Prism from "prismjs";
import "prismjs/themes/prism-okaidia.css";
import "prismjs/components/prism-markup-templating.min.js";
import "prismjs/components/prism-python.min.js";
import "prismjs/components/prism-javascript.min.js";
import "prismjs/components/prism-css.min.js";
import "prismjs/components/prism-clike.min.js";
import "prismjs/components/prism-bash.min.js";
import "prismjs/components/prism-django.min.js";
import "prismjs/components/prism-docker.min.js";
import "prismjs/components/prism-git.min.js";
import "prismjs/components/prism-go.min.js";
import "prismjs/components/prism-http.min.js";
import "prismjs/components/prism-ignore.min.js";
import "prismjs/components/prism-json.min.js";
import "prismjs/components/prism-kotlin.min.js";
import "prismjs/components/prism-markdown.min.js";
import "prismjs/components/prism-sql.min.js";
import "prismjs/components/prism-typescript.min.js";

marked.setOptions({
  langPrefix: "language-",
  pedantic: false,
  gfm: true,
  breaks: false,
  sanitize: false,
  smartLists: true,
  smartypants: false,
  xhtml: false,
});

export default {
  name: "Post",
  components: { BackButton },
  data: () => ({
    postName: undefined,
    markdownSource: undefined,
  }),
  methods: {
    isXOverflown(element) {
      return element.scrollWidth > element.clientWidth;
    },
    codeOverflow() {
      let codeBlocks = document.getElementsByTagName("pre");
      for (let i = 0; i < codeBlocks.length; ++i) {
        let el = codeBlocks[i].getElementsByTagName("code")[0];
        codeBlocks[i].classList.remove("overflown-code");
        codeBlocks[i].classList.add("little-code");
        if (this.isXOverflown(el)) {
          codeBlocks[i].classList.remove("little-code");
          codeBlocks[i].classList.add("overflown-code");
        } else {
          codeBlocks[i].classList.remove("overflown-code");
          codeBlocks[i].classList.add("little-code");
        }
      }
    },
    resizeHandler() {
      this.codeOverflow();
    },
  },
  created() {
    this.postName = this.$route.params.postName;
    const markdownSource = require(`@/posts/${this.$route.params.postName}`);
    this.markdownSource = markdownSource.default;
    window.addEventListener("resize", this.resizeHandler);
  },
  destroyed() {
    window.removeEventListener("resize", this.resizeHandler);
  },
  mounted() {
    Prism.highlightAll();
    this.codeOverflow();
  },
  computed: {
    markdownToHtml() {
      return marked.parse(this.markdownSource);
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
@media screen and (min-width: 601px) {
  .post-page {
    font-size: 20px;
  }
}
@media screen and (max-width: 600px) {
  .post-page {
    font-size: 18px;
  }
}

.post-page h1 {
  font-size: 40px;
}

.post-page blockquote {
  width: 90%;
  font-size: 17px;
  padding-left: 10px;
  padding-top: 5px;
  padding-right: 10px;
  padding-bottom: 1px;
  background-color: #24283b;
  border-top-right-radius: 20px;
  border-bottom-right-radius: 20px;
  border-left: 5px solid #565f89;
  box-shadow: 5px 5px 10px #13131b, -5px -5px 10px #212331;
}
.post-page blockquote p {
  margin: 0;
  padding-bottom: 5px;
}

.post-page pre.little-code {
  background-color: #24283b;
  border-radius: 20px;
  color: #a9b1d6;
  margin-top: 20px;
  margin-bottom: 20px;
  overflow: hidden;
  border: solid 2px #414868;
  box-shadow: 5px 5px 10px #13131b, -5px -5px 10px #212331;
}
.post-page pre.overflown-code {
  background-color: #24283b;
  width: 97vw;
  position: relative;
  left: calc(-48.5vw + 50%);
  color: #a9b1d6;
  margin-top: 20px;
  margin-bottom: 20px;
  overflow: hidden;
  border: solid 2px #414868;
  border-radius: 20px;
  padding: 0;
  padding-top: 10px;
  padding-bottom: 10px;
  box-shadow: inset 11px 11px 38px #1a1d2a, inset -11px -11px 38px #2e334c;
}
.post-page pre.overflown-code code {
  padding-left: 10px;
  padding-bottom: 10px;
  padding-top: 10px;
}
@media screen and (min-width: 601px) {
  .post-page pre {
    font-size: 18px;
  }
}
@media screen and (max-width: 600px) {
  .post-page pre {
    font-size: 13px;
  }
}

.theme--dark.v-application code {
  background-color: #ffffff00;
  padding: 2px;
}
pre code {
  display: block;
  overflow-x: auto;
}
code .token.number {
  color: #ff9e64;
}
code .token.keyword {
  color: #bb9af7;
}
code .token.operator {
  color: #7dcfff;
}
code .token.punctuation {
  color: #7aa2f7;
}
code .token.string-interpolation {
  color: #9ece6a;
}
code .token.builtin {
  color: #2ac3de;
}
code .token.string {
  color: #9ece6a;
}

.post-page img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  margin-top: 20px;
  margin-bottom: 20px;
  width: 95%;
  max-width: 800px;
  max-height: 500px;
  transition: all 0.1s ease-in-out;
  border: solid 5px #1a1b26;
  border-radius: 20px;
  box-shadow: 5px 5px 10px #13131b, -5px -5px 10px #212331;
}
.post-page img:hover {
  transition: all 0.1s ease-in-out;
  box-shadow: 30px 30px 60px #13141c, -30px -30px 60px #212230;
}

.post-page input[type="checkbox"] {
  width: 20px;
  height: 20px;
}
</style>
