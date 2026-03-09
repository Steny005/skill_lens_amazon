import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from utils.video_utils import extract_audio, transcribe_audio
from agents.step_agent import extract_steps
st.title("Tutorial Step Extractor")
st.write("Upload a tutorial video to extract clear learning steps.")
video = st.file_uploader("Upload Video")
if video:
    with open("temp_video.mp4", "wb") as f:
        f.write(video.read())

    st.video("temp_video.mp4")
    st.write("Extracting audio...")
    audio = extract_audio("temp_video.mp4")
    transcript = transcribe_audio(audio)
    st.write(transcript)
    steps=extract_steps(transcript)
    st.write("Extracted Steps:")
    st.write(steps)