import cv2
import time

# Initialize the video capture object
video = cv2.VideoCapture(1)

# Delay to allow the camera to start (1-second delay)
time.sleep(1)

# Infinite loop to continuously capture and display video frames
while True:
    # Read a frame from the video capture object
    check, frame = video.read()

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale frame
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # Display the captured frame in a window titled "My Video"
    cv2.imshow("My Video", gray_frame_gau)

    # Wait for a key press
    key = cv2.waitKey(1)

    # Break the loop if the 'q' key is pressed
    if key == ord("q"):
        break

# Release the video capture object
video.release()


