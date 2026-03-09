from moviepy import VideoFileClip
def extract_audio(video_path, output="audio.mp3"):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output)
    return output

from faster_whisper import WhisperModel
model = WhisperModel("base")
def transcribe_audio(audio_path):
    segments, info = model.transcribe(audio_path)
    transcript=""
    for segment in segments:
        transcript+=segment.text+" "
    return transcript