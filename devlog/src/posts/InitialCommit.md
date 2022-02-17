# The largest heading

## The second largest heading

### Headings 3

#### Heading 4

##### Heading 5

###### The smallest heading

Text that is not a quote

> Text that is a quote

Use `git status` to list all new or modified files that haven't yet been committed.
Some basic Git commands are:

```git
git status
git add
git commit
```

```python
from os import listdir, getcwd
from os.path import isfile, join
from json import dump, load
from datetime import datetime


POSTS_DIR = f"{getcwd()}/src/posts/"

posts = [f for f in listdir(POSTS_DIR) if isfile(join(POSTS_DIR, f))]

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

for post in new_posts:
    print(f"New post: {post}")
    title = input("Title: ")
    tags = list(input("Tags: ").split(', '))
    image = input("Image: ")
    post_data = {
        "title": title,
        "tags": tags,
        "image": image,
        "timestamp": datetime.now().strftime("%H:%M %A, %-d %b")
    }
    posts_data[post] = post_data
    print("Post added!")

with open(f'{getcwd()}/src/postsData.json', 'w') as posts_data_file:
    dump(posts_data, posts_data_file, ensure_ascii=False, indent=2)
```

![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Velit dignissim sodales ut eu sem integer vitae justo. Metus aliquam eleifend mi in. Est placerat in egestas erat imperdiet sed euismod. Accumsan lacus vel facilisis volutpat est. Id donec ultrices tincidunt arcu non sodales neque. Pellentesque elit ullamcorper dignissim cras tincidunt lobortis feugiat. Turpis egestas integer eget aliquet nibh praesent tristique. Elit pellentesque habitant morbi tristique. Vitae elementum curabitur vitae nunc sed velit dignissim sodales. Aliquet enim tortor at auctor urna nunc.

Scelerisque in dictum non consectetur a erat nam. Purus sit amet luctus venenatis lectus. Semper eget duis at tellus at urna condimentum mattis. Feugiat in ante metus dictum at tempor commodo ullamcorper a. Venenatis lectus magna fringilla urna porttitor rhoncus dolor purus. Lorem ipsum dolor sit amet consectetur adipiscing elit. Euismod quis viverra nibh cras pulvinar mattis nunc sed. Facilisis volutpat est velit egestas dui id ornare arcu. Faucibus pulvinar elementum integer enim neque volutpat. Sem nulla pharetra diam sit. Purus sit amet luctus venenatis lectus magna. Fermentum iaculis eu non diam.

- George Washington
- John Adams
- Thomas Jefferson

1. James Madison
2. James Monroe
3. John Quincy Adams

4. First list item
   - First nested list item
     - Second nested list item

- [x] #739
- [ ] <https://github.com/octo-org/octo-repo/issues/740>
- [ ] Add delight to the experience when all tasks are complete :tada:

@octocat :+1: This PR looks great - it's ready to merge! :anger:

```bash
$ echo "hello world"
hello world
```
