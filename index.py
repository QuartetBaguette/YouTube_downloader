from pytube import YouTube
import os

print("What video would you like to download? (YouTube url only)")
link = input()

YouTube(link).streams.get_highest_resolution().download(f'/Users/{os.getlogin()}/Downloads')