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
for post in posts_data:
    old_posts.append(post["file"])
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
        "file": post,
        "tags": tags,
        "image": image,
        "timestamp": datetime.now().strftime("%H:%M %A, %-d %b")
    }
    posts_data.append(post_data)
    print("Post added!")

with open(f'{getcwd()}/src/postsData.json', 'w') as posts_data_file:
    dump(posts_data, posts_data_file, ensure_ascii=False, indent=2)
