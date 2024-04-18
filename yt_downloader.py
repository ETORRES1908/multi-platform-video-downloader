from pytube import YouTube
from utils import check_path

def progress_check(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f'Download progress... {int(percentage_of_completion)}%')

def yt_download(link, path, prefix):
    check_path(path)
    youtubeObject = YouTube(url=link,on_progress_callback=progress_check)
    #video = youtubeObject.streams.filter(adaptive=True).filter(mime_type='video/webm').first()
    #TODO: Get the highest resolution, function get_highest_resolution dont get the highest resolution for some reason
    video = youtubeObject.streams.get_highest_resolution()
    try:
        if(video != None):
            video.download(output_path=path, filename_prefix=prefix)
    except:
        print("An error has occurred")

    print("Download is completed successfully")