import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load image
image = Image.open('your_image.png')

# Create an empty figure for animation
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Display the image
img_plot = ax.imshow(image, aspect='auto', extent=[0, 2, 0, 2])

# Update function for the animation
def update(frame):
    # Move the image by updating its position
    img_plot.set_extent([frame, frame+2, 0, 2])  # Moves the image along the X-axis
    return img_plot,

# Create an animation
ani = FuncAnimation(fig, update, frames=range(0, 10), blit=True)

# Display animation in Streamlit
st.pyplot(fig)
