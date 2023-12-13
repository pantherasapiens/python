import pyttsx3
import cv2
import numpy as np

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Text to be spoken by the avatar
text_to_say = "Hello, I am your talking avatar. How can I assist you today?"

# Set properties for the speech (adjust as needed)
engine.setProperty("rate", 150)  # Speed of speech (words per minute)
engine.setProperty("volume", 1.0)  # Volume level (0.0 to 1.0)

# Load your background image
background_image = cv2.imread('avatar.jpeg')  # Replace with your image path

# Function to generate a video of the avatar reading text using OpenCV
def generate_avatar_video(text, output_file):
    video_frames = []

    for sentence in text.split('. '):
        # Generate speech for the current sentence
        engine.say(sentence)
        engine.runAndWait()

        # Create a copy of the background image to avoid modifying the original
        frame = background_image.copy()

        # Overlay the text on the frame
        cv2.putText(frame, sentence, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Set the duration for the frame (adjust as needed)
        frame_duration = int(len(sentence) / 10)  # You can change the duration logic

        # Duplicate the frame for the specified duration
        for _ in range(frame_duration * 24):  # Assuming 24 frames per second
            video_frames.append(frame)

    # Write the frames to a video file
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, 24, (background_image.shape[1], background_image.shape[0]))
    
    for frame in video_frames:
        out.write(frame)

    out.release()

if __name__ == "__main__":
    output_file = "avatar_reading_text_with_image.avi"
    generate_avatar_video(text_to_say, output_file)
