import cv2
import os

def extract_frames(video_path, output_folder="frames", interval=30):

    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    saved_frame = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_count % interval == 0:
            frame_path = f"{output_folder}/frame_{saved_frame}.jpg"
            cv2.imwrite(frame_path, frame)
            saved_frame += 1

        frame_count += 1

    cap.release()

    return output_folder