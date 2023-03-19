from pytube import YouTube
import os

while True:
    print("\033[1;33m What video would you like to download? (YouTube url only)")
    link = input()

    audio = YouTube(link).streams.filter(only_audio=True).first()

    path = f'/Users/{os.getlogin()}/Downloads/' + YouTube(link).title + '.mp3'
    fileExists = os.path.isfile(path)

    try:
        if fileExists:
            raise FileExistsError()

        download = audio.download(f'/Users/{os.getlogin()}/Downloads')

        base, ext = os.path.splitext(download)

        new_file = base + '.mp3'

        os.rename(download, new_file)
        print("\033[1;32m File downloaded successfully! \n")
    except FileExistsError:
        print("\033[0;31m File already exists in folder. \n")
    except Exception:
        print("\033[0;31m Something went wrong, please try again. \n")