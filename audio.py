from pytube import YouTube


def get_audio(video_id):
    try:    
        # Download audio from YouTube video
        video = YouTube(f'https://www.youtube.com/watch?v={video_id}')
        audio = video.streams.filter(only_audio=True, file_extension='webm').first()
        audio.download(filename="audio.mp3")
        return True
    except:
        return False


# video_id = '8i3yvypt1F4'
# get_audio(video_id)
