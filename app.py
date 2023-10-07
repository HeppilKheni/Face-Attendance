from fastapi import FastAPI, HTTPException
from datetime import datetime
import face_recognition
import time
import cv2

app = FastAPI()

@app.post("/capture_image/{username}")
async def capture_image(username: str):
    video_capture = cv2.VideoCapture(0)
    time.sleep(5)
    t = 0

    while True:
        ret, frame = video_capture.read()
        if not ret:
            raise HTTPException(status_code=500, detail="Error capturing frame")

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(frame_rgb)
        
        image = f'/Users/kirtan/Desktop/User/images/{username}.jpg'
        face_encodings = face_recognition.face_encodings(frame_rgb, face_locations)
        cv2.imwrite(image, frame)
        t += 1

        if t == 1:
            print(f"{username} : {face_encodings}" )
            return {f"{username} : {face_encodings}"}
