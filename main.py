from fileinput import filename
import time
import os
from twitter_downloader import download_twitter_video
from yt_downloader import yt_download
from pathlib import Path
from utils import twitter_url_checker, youtube_url_checker
# OUTPUT_PATH = os.path.join(os.getcwd(), "videos")
OUTPUT_PATH = os.path.join(Path.home(), "Downloads")
PLATFORMS = {1: 'Youtube', 2: 'Twitter'}

def main():
    print("Select wich platform you want: ")
    print("1. Youtube")
    print("2. Twitter")
    # TODO: Add more platforms
    
    platform = int(input())
    selected_platform = PLATFORMS[platform]
    link = input(f"Enter the {selected_platform} video URL: ")
    PREFIX = f'{time.time()}_{selected_platform}_'

    match selected_platform:
        case "Youtube":
            youtube_url_checker(link)
            yt_download(link, OUTPUT_PATH, PREFIX)
        case "Twitter":
            twitter_url_checker(link)
            download_twitter_video(link, PREFIX)
    print("Do you want to download another video? (y/n)")
    answer = input()
    if answer.lower() == 'y':
        main()
    else:
        # print("Thank you for using the program. Goodbye!")
        print("Done!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")