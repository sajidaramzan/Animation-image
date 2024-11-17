import streamlit as st
import cv2
import numpy as np
from PIL import Image

# File uploader to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Load the uploaded image
    image = Image.open(uploaded_file)

    # Convert image to OpenCV format
    image_cv = np.array(image)

    # Set up video writer (FourCC codec and frame rate)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' for .mp4 file
    frame_rate = 30  # frames per second
    frame_size = (image_cv.shape[1], image_cv.shape[0])  # (width, height)
    
    # Create a VideoWriter object to save the video
    video_writer = cv2.VideoWriter('animated_image.mp4', fourcc, frame_rate, frame_size)

    # Animate and write frames
    for i in range(100):  # 100 frames for the animation
        # Create a blank frame (white background)
        frame = np.ones_like(image_cv) * 255  # A white background
        
        # Calculate the position to move the image (moving it along the X-axis)
        x_offset = i  # Move the image horizontally
        
        # Copy the image onto the blank frame
        frame[0:image_cv.shape[0], x_offset:x_offset+image_cv.shape[1]] = image_cv
        
        # Write the frame to the video
        video_writer.write(frame)

    # Release the video writer
    video_writer.release()

    # Display video on Streamlit
    st.video('animated_image.mp4')
