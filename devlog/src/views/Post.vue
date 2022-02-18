<template>
  <div class="post-page">
    <div style="height: 5px"></div>
    <h1>{{ title }}</h1>
    <span style="font-size: 18px">{{ timestamp }}</span>
    <v-chip-group column>
      <v-chip v-for="tag in tags" :key="tag" color="#bb9af7" outlined>{{
        tag
      }}</v-chip>
    </v-chip-group>
    <div style="height: 10px"></div>
    <div v-html="markdownToHtml"></div>
    <div style="height: 30px"></div>
    <BackButton />
    <div style="height: 30px"></div>
  </div>
</template>

<script>
import BackButton from "@/components/BackButton.vue";
import postsDataJson from "@/postsData.json";
import { marked } from "marked";
import emoji from "node-emoji";
import Prism from "prismjs";
import "prismjs/themes/prism-okaidia.css";
import "prismjs/components/prism-markup-templating.min.js";
import "prismjs/components/prism-python.min.js";
import "prismjs/components/prism-javascript.min.js";
import "prismjs/components/prism-css.min.js";
import "prismjs/components/prism-clike.min.js";
import "prismjs/components/prism-c.min.js";
import "prismjs/components/prism-cpp.min.js";
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
import "prismjs/components/prism-csharp.min.js";
import "prismjs/components/prism-elm.min.js";
import "prismjs/components/prism-smalltalk.min.js";
import "prismjs/components/prism-java.min.js";

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
    markdownSource: undefined,
    title: undefined,
    timestamp: undefined,
    tags: [],
  }),
  computed: {
    markdownToHtml() {
      return marked.parse(this.markdownSource);
    },
  },
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
    replaceCheckboxes() {
      let inputs = document.getElementsByTagName("input");
      while (inputs.length > 0) {
        for (let i = 0; i < inputs.length; ++i) {
          if (inputs[i].type == "checkbox") {
            if (inputs[i].checked)
              inputs[i].outerHTML =
                "<span style='color: #00ff00; font-size: 25px'>✔</span>";
            else
              inputs[i].outerHTML =
                "<span style='color: #ff0000; font-size: 25px'>✘</span>";
          }
        }
        inputs = document.getElementsByTagName("input");
      }
    },
    labelCodeBlocks() {
      const langPrefix = "language-";
      let codeBlocks = document.getElementsByTagName("pre");
      for (let i = 0; i < codeBlocks.length; ++i) {
        if (codeBlocks[i].getElementsByTagName("code").length > 0) {
          let language = undefined;
          for (let j = 0; j < codeBlocks[i].classList.length; ++j) {
            if (codeBlocks[i].classList[j].startsWith(langPrefix)) {
              language = codeBlocks[i].classList[j].substring(
                langPrefix.length
              );
              break;
            }
          }
          if (language) {
            language = language.charAt(0).toUpperCase() + language.slice(1);
            let label = document.createElement("span");
            label.classList.add("codeblock-label");
            label.innerHTML = language;
            codeBlocks[i].appendChild(label);
          }
        }
      }
    },
    getPostData() {
      this.title = postsDataJson[this.$route.params.postName].title;
      this.timestamp = postsDataJson[this.$route.params.postName].timestamp;
      this.tags = postsDataJson[this.$route.params.postName].tags;
    },
    setMarkdownSource() {
      const markdownSource = require(`@/posts/${this.$route.params.postName}`);
      this.markdownSource = markdownSource.default;
      const replacer = (match) => emoji.emojify(match);
      this.markdownSource = this.markdownSource.replace(/(:.*:)/g, replacer);
    },
  },
  created() {
    this.getPostData();
    this.setMarkdownSource();
    window.addEventListener("resize", this.resizeHandler);
  },
  destroyed() {
    window.removeEventListener("resize", this.resizeHandler);
  },
  mounted() {
    Prism.highlightAll();
    this.codeOverflow();
    this.replaceCheckboxes();
    this.labelCodeBlocks();
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

.post-page blockquote {
  width: 90%;
  font-size: 17px;
  margin-bottom: 10px;
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
  width: 96vw;
  position: relative;
  left: calc(-48vw + 50%);
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

.post-page pre {
  position: relative;
  padding-top: 30;
}
.post-page ol li pre {
  margin-left: -12px;
}
.post-page .codeblock-label {
  position: absolute;
  top: 2px;
  right: 10px;
  font-size: 16px;
  text-shadow: 0px 0px #ffffff00;
  color: #565f89;
}
@media screen and (min-width: 601px) {
  .post-page .codeblock-label {
    font-size: 16px;
  }
}
@media screen and (max-width: 600px) {
  .post-page .codeblock-label {
    font-size: 11px;
  }
}

.theme--dark.v-application code {
  background-color: #ffffff00;
  padding: 2px;
  text-shadow: 0px 0px #ffffff00;
  font-family: monospace, monospace;
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
code .token.class-name {
  color: #9ece6a;
}
code .token.function {
  color: #7aa2f7;
}
code .token.char {
  color: #9ece6a;
}
code .token.symbol {
  color: #bb9af7;
}
code .token.regex {
  color: #e0af68;
}
code .token.url {
  color: #73daca;
}
code .token.constant {
  color: #ff9e64;
}
code .token.property {
  color: #7dcfff;
}
code .token.important {
  color: #f7768e;
}
code .token.comment {
  color: #565f89;
}
code .token.tag {
  color: #f7768e;
}
code .token.attr-name {
  color: #bb9af7;
}
code .token.attr-value {
  color: #c0caf5;
}
code .token.namespace {
  color: #7dcfff;
  opacity: 1;
}
code .token.prolog {
  color: #565f89;
}
code .token.doctype {
  color: #565f89;
}
code .token.cdata {
  color: #565f89;
}
code .token.entity {
  color: #ff9e64;
}
code .token.atrule {
  color: #bb9af7;
}
code .token.selector {
  color: #2ac3de;
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
