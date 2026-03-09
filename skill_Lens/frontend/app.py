import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from utils.frame_extractor import extract_frames

st.title("SkillLens AI Tutor")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Tutorial Video")
    video = st.file_uploader("Upload Tutorial", type=["mp4","mov","avi"])

    if video:
        # Save uploaded video
        with open("temp_video.mp4", "wb") as f:
            f.write(video.read())

        st.video("temp_video.mp4")

        st.write("Extracting frames...")

        # Run frame extractor
        frames_folder = extract_frames("temp_video.mp4")

        frames = sorted(os.listdir(frames_folder))

with col2:
    st.subheader("Current Step")

    if video and len(frames) > 0:
        first_frame = os.path.join(frames_folder, frames[0])
        st.image(first_frame)
        st.write("Step 1: Follow the reference action")
    else:
        st.write("Upload a tutorial to generate steps")

st.subheader("Practice Area")

camera = st.camera_input("Show your action")