import cv2
import time
from PIL import Image
import numpy as np

# Folder
folder = "frames"

# Initialize the webcam
cap = cv2.VideoCapture(1)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

# Wait for the camera to initialize and adjust light levels
time.sleep(2)

while True:
    ret, frame = cap.read()
    if ret:
        # Convert the frame to a PIL image
        pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Resize the image
        max_size = 250
        ratio = max_size / max(pil_img.size)
        new_size = tuple([int(x*ratio) for x in pil_img.size])
        resized_img = pil_img.resize(new_size, Image.LANCZOS)

        # Convert the PIL image back to an OpenCV image
        frame = cv2.cvtColor(np.array(resized_img), cv2.COLOR_RGB2BGR)

        # Save the frame as an image file
        print("📸 Say cheese! Saving frame.")
        path = f"{folder}/frame.jpg"
        cv2.imwrite(path, frame)
    else:
        print("Failed to capture image")

    # Wait for 2 seconds
    time.sleep(30)

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
