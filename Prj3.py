import cv2
import pytesseract

# Set the path to the Tesseract executable (modify this according to your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the video file
video_path = 'your_video.mp4'  # Replace with your video file
cap = cv2.VideoCapture(video_path)

# Loop through the video frames and extract text using OCR
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for better OCR results (optional)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the frame
    text = pytesseract.image_to_string(gray_frame)

    # Print the extracted text from each frame
    print(text)

    # Display the frame (optional)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
