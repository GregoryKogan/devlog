![Markdown logo](https://texterra.ru/upload/iblock/933/header.jpg)

## What are we doing here?

In this article you will learn how to:
- Make structure for `Vue` markdown blog
- Render markdown files inside Vue
- Modify markdown rendering CSS to alter it's appearance
- Use `hightlight.js` or `Prism.js` for syntax highlighting
- Deploy your blog to github pages

## Initialization
Create new Vue project using `vue-cli`

```bash
vue create my-blog
```

Select `Manually select features` option. Make sure project uses `Router` and `Vue2.x`. You should not use `history mode for router`. Other settings are not important in our case.

```bash
cd my-blog
npm run serve
```

Delete all default project files such as `components/HelloWorld.vue`, `views/AboutView.vue` and so on.

Now we are ready to write our own code!

## Project structure
Create `postsData.json` file inside `src` folder. Put empty curly brackets in it

```Json
{}
```

Create `posts` folder inside `src`. And create 'MyFirstPost.md` file inside it.

```Markdown
<!-- MyFirstPost.md -->

# This is my first post

## Some basic Markdown syntax:

#### Normal text

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Adipiscing elit ut aliquam purus sit amet luctus. Amet luctus venenatis lectus magna fringilla urna porttitor rhoncus. Mauris pharetra et ultrices neque ornare aenean. Sed lectus vestibulum mattis ullamcorper velit sed ullamcorper morbi. Interdum consectetur libero id faucibus nisl tincidunt. Sed blandit libero volutpat sed cras ornare arcu dui. Id consectetur purus ut faucibus pulvinar elementum. Egestas integer eget aliquet nibh.

### Code block

<!-- You should remove "\" before "```"  -->
\```JavaScript
for (let i = 0; i < 100; i++) {
    console.log("I love Markdown!");
}
\```


### Quotes

Some normal text
> Very smart quote
> > Indented quoute


### Lists
- First
- Second
- Third

1. First
2. Second
3. Third

### Image

![Markdown logo](https://texterra.ru/upload/iblock/933/header.jpg)


### Check lists

- [ ] Todo 1
- [x] Todo 2
- [ ] Todo 3
- [x] Todo 4
```
Now we need to write python script for managing our posts. Create `AddPost.py` file inside `src` folder.

```Python
from os import listdir, getcwd
from os.path import isfile, join
from json import dump, load
from datetime import datetime


# Reading all posts from src/posts/
POSTS_DIR = f"{getcwd()}/src/posts/"

posts = [f for f in listdir(POSTS_DIR) if isfile(join(POSTS_DIR, f))]

# Getting all new posts
new_posts = []
with open(f'{getcwd()}/src/postsData.json') as posts_data_file:
    posts_data = load(posts_data_file)
old_posts = []
for post_file in posts_data:
    old_posts.append(post_file)
for post in posts:
    if post not in old_posts:
        new_posts.append(post)

print(f"{len(new_posts)} new posts found!")

# Adding new posts to postsData.json
for post in new_posts:
    # Asking user for post's title, tags and image
    print(f"New post: {post}")
    title = input("Title: ")
    tags = list(input("Tags: ").split(', '))  # Tags are separated by ", "
    image = input("Image: ")
    post_data = {
        "title": title,
        "tags": tags,
        "image": image,
        "timestamp": datetime.now().strftime("%H:%M %A, %-d %b")
    }
    posts_data[post] = post_data
    print("Post added!")

# Writing data to postsData.json
with open(f'{getcwd()}/src/postsData.json', 'w') as posts_data_file:
    dump(posts_data, posts_data_file, ensure_ascii=False, indent=2)
```

Let's run it!

```Bash
python3 src/AddPost.py
```

Result should look like this:
![AddPost.py script output](https://i.ibb.co/ZWSrCHB/Arco-Linux-2022-02-20-22-41-37.png)

Now `postsData.json` is populated with new data:

```Json
{
  "MyFirstPost.md": {
    "title": "My first post",
    "tags": [
      "some",
      "tags",
      "hello",
      "mom"
    ],
    "image": "https://www.denofgeek.com/wp-content/uploads/2019/11/Attack-on-Titan-Season-4-Release-Date-Trailer-News.jpg",
    "timestamp": "22:39 Sunday, 20 Feb"
  }
}
```

It's time to create a home page. In `views/Home.vue` we will import our generated `postsData.json` file and use it to show clickable previews of all our posts.

```Markup
// views/Home.vue

<template>
  <div class="home-page">
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
```

It won't work for now, because we're using `PostPreview` component which is not existing at the moment. Let's create it! Add `PostPreview.vue` file to `src/components/` folder.

```Markup
// components/PostPreview.vue

<template>
  <div class="post-preview" @click="openPost">
    <span>{{ post.title }}</span>
    <div style="height: 10px"></div>
    <span>{{ post.timestamp }}</span>
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
  color: #fff;
  background: #181818;
  padding: 10px;
  border-radius: 20px;
}
</style>
```

Now home page should look something like this:

![Home page](https://imgur.com/man0d8B.png)

But if we click on it, nothing really happens. To fix this we need to create `views/Post.vue` file and configure our `Router` properly.

```JavaScript
// src/router/index.js

import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Post from "../views/Post.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/post/:postName",
    name: "Post",
    component: Post,
  },
];

const router = new VueRouter({
  mode: "hash",
  base: process.env.BASE_URL,
  routes,
});

export default router;
```

Post view

```Markup
// views/Post.vue

<template>
  <div class="post-page">
    <div style="height: 5px"></div>
    <h1>{{ title }}</h1>
    <span style="font-size: 18px">{{ timestamp }}</span>
    <div style="height: 10px"></div>
    <div v-html="markdownToHtml"></div>
    <div style="height: 30px"></div>
  </div>
</template>

<script>
import postsDataJson from "@/postsData.json";
import { marked } from "marked";

export default {
  name: "PostView",
  data: () => ({
    markdownSource: undefined,
    title: undefined,
    timestamp: undefined,
  }),
  computed: {
    markdownToHtml() {
      return marked.parse(this.markdownSource);
    },
  },
  methods: {
    getPostData() {
      this.title = postsDataJson[this.$route.params.postName].title;
      this.timestamp = postsDataJson[this.$route.params.postName].timestamp;
      this.tags = postsDataJson[this.$route.params.postName].tags;
    },
    setMarkdownSource() {
      const markdownSource = require(`@/posts/${this.$route.params.postName}`);
      this.markdownSource = markdownSource.default;
    },
  },
  created() {
    this.getPostData();
    this.setMarkdownSource();
  },
};
</script>

<style>
.post-page {
  width: 90%;
  margin-left: auto;
  margin-right: auto;
}
</style>
```

For markdown rendering we'll use `Marked.js` library.

```Bash
npm install --save marked
```

To load `.md` files we need to specify correct loader for them. 
<br />
Install `raw-loader`

```Bash
npm install -D raw-loader
```

Add this to `vue.config.js`:

```JavaScript
module.exports = {
  ...
  configureWebpack: {
    module: {
      rules: [
        {
          test: /\.md$/,
          loader: "raw-loader",
        },
      ],
    },
  },
};
```

Hooray! We got our markdown rendered in browser!

![Post page](https://imgur.com/ybKt5tL.png)

That's it! Now you can build your blog on top of this structure.

**Bonus - rendering emojis**

If you want to render emojis written like this - \:sunglasses\:, use node-emoji library.

```Bash
npm install --save node-emoji
```

```JavaScript
<script>
import emoji from "node-emoji";

export default {
  methods: {
    setMarkdownSource() {
      const markdownSource = require(`@/posts/${this.$route.params.postName}`);
      this.markdownSource = markdownSource.default;
      const replacer = (match) => emoji.emojify(match);
      this.markdownSource = this.markdownSource.replace(/(:.*:)/g, replacer);
    },
  },
};
</script>
```

### Styling Markdown with CSS

Here are some examples of styling html-rendered markdown
with CSS. Of course you can change and adapt anything here 
to satisfy your project's needs.

#### Preparation
In `Post.vue`:
```CSS
<style>
/* ... */
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
/* ... */
</style>
```

In `App.vue`:
```CSS
<style>
/* ... */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
#app {
  background-color: #1a1b26;
  color: #c0caf5;
}
/* ... */
</style>
```

Now markdown should look like this:

![Styled md](https://imgur.com/roIaY98.png)

#### Quotes

In `Post.vue`:
```CSS
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
```

Now quotes should look like this:

![Styled quotes](https://imgur.com/BYg5qKh.png)

#### Images

In `Post.vue`:
```CSS
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
```

Now images should look like this:

![Styled image](https://imgur.com/0kc8UjE.png)

##### Bonus - image hosting

If you prefer to store images locally, you can, but I don't recommend doing so because it will slow down the blog's page loading. Storing your images somewhere on the internet is a better idea. I use [Imgur](https://imgur.com/), but there are plenty other services for that.

#### Checklists

Default look of checkboxes is goddamn disgusting.

![Disgusting checkboxes](https://imgur.com/LrPrGrS.png)

I tried to style those with CSS, but it didn't work, so I used JavaScript. As long as these checkboxes are static we can simply replace them with some gorgeous emojis.

In `Post.vue`:
```JavaScript
methods: {
  // ... //
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
},
mounted() {
  // ... //
  this.replaceCheckboxes();
},
```

Result:

![new checklists](https://imgur.com/XTpeHkj.png)

#### Code blocks

In `Post.vue`:

```CSS
.post-page pre {
  position: relative;
  padding-top: 30;
  background-color: #24283b;
  border-radius: 20px;
  color: #a9b1d6;
  margin-top: 20px;
  margin-bottom: 20px;
  overflow: hidden;
  border: solid 2px #414868;
  box-shadow: 5px 5px 10px #13131b, -5px -5px 10px #212331;
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
```

This is how it looks now:

![Weird code block](https://imgur.com/WxN9Uqf.png)

Weird, isn't it? Well, it's all going to be fixed after we apply syntax highlighting.

**Bonus 1 - large code snippets**

If you want to apply different styles for small and large code snippets, you can assign CSS classes to them like this:

```JavaScript
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
  window.addEventListener("resize", this.resizeHandler);
},
destroyed() {
  window.removeEventListener("resize", this.resizeHandler);
},
mounted() {
  this.codeOverflow();
},
```

**Bonus 2 - code block labeling**

If you want to label yor code blocks (add that little thingy with language name), you can do it like this:

```JavaScript
methods: {
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
},
mounted() {
  this.labelCodeBlocks();
},
```

### Syntax highlighting

Of course you can follow `Marked.js` [documentation](https://marked.js.org/using_advanced#highlight) and use `highlight.js` like this:

```Bash
npm install --save highlight.js
```

```JavaScript
// Set options
// `highlight` example uses https://highlightjs.org
marked.setOptions({
  renderer: new marked.Renderer(),
  highlight: function(code, lang) {
    const hljs = require('highlight.js');
    const language = hljs.getLanguage(lang) ? lang : 'plaintext';
    return hljs.highlight(code, { language }).value;
  },
  langPrefix: 'hljs language-', // highlight.js css expects a top-level 'hljs' class.
});
```

But, I hate how `highlight.js` functions, so I prefer `Prism.js` as it's more advanced and customizable.

```Bash
npm install --save prismjs
```

```JavaScript
<style>
import Prism from "prismjs";
import "prismjs/themes/prism-okaidia.css"; // could be any prismjs theme

marked.setOptions({
  langPrefix: "language-",
  // ... //
});

export default {
  // ... //
  mounted() {
    Prism.highlightAll();
    // ... //
  },
};
</style>
```

Now our codeblock looks like this:

![Highlighted codeblock](https://imgur.com/nbNDock.png)

Better than before, but doesn't really fit. Let's customize it! `Prism.js` tokenized our codeblock and we can style it with CSS.

```CSS
.post-page code {
  color: #a9b1d6;
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
code .token.variable {
  color: #c0caf5;
}
```

Now it looks perfectly:

![styled code](https://imgur.com/dS7spz4.png)

You can find list of all `Prism.js` tokens [here](https://prismjs.com/tokens.html).

If you want highlighting for any specific language, you can import it like this:

```JavaScript
// Example:
// import "prismjs/components/prism-<lang-name>.min.js";
import "prismjs/components/prism-python.min.js";
import "prismjs/components/prism-typescript.min.js";
import "prismjs/components/prism-json.min.js";
// ... //
```

You can read list of all supported languages [here](https://prismjs.com/)

#### Result

Result of all of above should look like this:
![CSS result](https://imgur.com/UpOP6uA.png)  

### Deployment

#### Preparation

For our website to function properly on github pages, we need to
specify `public path` variable in `vue.config.js` file in project's
root directory. 

```JavaScript
module.exports = {
  publicPath: process.env.NODE_ENV === "production" ? "/my-blog/" : "/",
  // ... //
};
```

Replace 'my-blog' with your repository's name.

#### Deploy script

Assuming you already got and connected a github repository, all you need to do is to create `deploy.sh` script in the root of your project and put this code into of it:

```Bash
#!/usr/bin/env sh

# abort on errors
set -e

# build
npm run build

# navigate into the build output directory
cd dist

# if you are deploying to a custom domain
# echo 'www.example.com' > CNAME

git init
git add -A
git commit -m 'deploy'

# if you are deploying to https://<USERNAME>.github.io
# git push -f git@github.com:<USERNAME>/<USERNAME>.github.io.git main

# if you are deploying to https://<USERNAME>.github.io/<REPO>
# git push -f git@github.com:<USERNAME>/<REPO>.git main:gh-pages

cd -
```

Do not forget to uncomment and fill necessary lines.

#### Deploy!

Make sure the script has run permissions. If not, you can give it
like this:

```Bash
sudo chmod +x deploy.sh
```

All set! Just run the script:

```Bash
./deploy.sh
```

We're done. This will build you project, create `gh-pages` branch
in your repository and deploy it.

You can read more about Vue deployment [here](https://cli.vuejs.org/guide/deployment.html).

### Bye-bye

Thank you for reading through this tutorial. I hope it helped you
in some way. All code for the blog you've just read is on [project's Github repo](https://github.com/GregoryKogan/Devlog).

Bye!
