# DevPSU Project 1
# Social Media API
# socialapi.py
# Do NOT change the names or parameters of any of the functions. You may add your own helper functions.

# Create an empty posts dictionary. 
# The key should be the name of the post and the value should be the content.
posts = { }

# ---- Edit below this line ----

# Helper function to check if a post exists in the dictionary
def post_exists(name):
    if name in posts:
        return True
    return False

# Get all posts and return them as a dictionary
def get_all_posts():
    return posts

# Get one post and return its name and content as a tuple (name, content)
# Return False if the post can't be found
def get_one_post(name):
    if post_exists(name):
        return name, posts[name]
    return False
    
# Save a single post
def save_post(name, content):
    posts[name] = content

# Delete a single post and return True
# Return False if the post can't be found
def delete_post(name):
    if post_exists(name):
        posts.pop(name)
        return True
    return False
    

