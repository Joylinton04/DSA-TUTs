import subprocess

def download_youtube_video():
    link = input('Enter your YouTube link: ')
    try:
        subprocess.run(['yt-dlp', link])
        print("Download completed successfully!")
    except Exception as e:
        print("An error occurred:", e)


download_youtube_video()