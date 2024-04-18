import os
import re

def check_path(path):
    if not os.path.exists(path):
        print("Folder not found, creating folder: " + path)
        os.makedirs(path)
        print("Folder created: " + path)
    print("Downloading to folder: " + path)

def twitter_url_checker(url):
    status = re.search("twitter.com|x.com", url)
    if status:
        print("Valid Twitter URL: " + url)
    else:
        print("Invalid Twitter URL: " + url)
        exit(1)
def youtube_url_checker(url):
    status = re.search("youtube.com", url)
    if status:
        print("Valid Youtube URL: " + url)
    else:
        print("Invalid Youtube URL: " + url)
        exit(1)