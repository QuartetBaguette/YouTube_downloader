from pytube import YouTube
import os

print("What video would you like to download? (YouTube url only)")
link = input()

video = YouTube(link).streams.get_highest_resolution()

download = video.download(f'/Users/{os.getlogin()}/Downloads')

base, ext = os.path.splitext(download)

new_file = base + '.mp3'
os.rename(download, new_file)