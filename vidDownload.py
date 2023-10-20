from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

video_directory = "./videos/"
audio_directory = "./audio/"

def download_video_from_youtube(link: str):
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()

    # download the video
    file_name = video.download(video_directory).rsplit("/", 1)[1]
    extract_audio_from_video(file_name)

def extract_audio_from_video(video_file: str):
    file_path = os.path.join(video_directory, video_file)
    wav_file_name = video_file.replace('.webm', '.wav').replace(".mp4", ".wav")
    video_clip = VideoFileClip(file_path)
    audio_clip = video_clip.audio

    if audio_clip is not None:
        audio_clip.write_audiofile(os.path.join(audio_directory, wav_file_name))
        video_clip.close()
        audio_clip.close()
    else:
        video_clip.close()


# example usage:
download_video_from_youtube('linkhere')



