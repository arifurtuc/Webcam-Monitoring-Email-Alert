import cv2
import time
import glob
from send_email import send_email

# Initialize the video capture object
video = cv2.VideoCapture(1)

# Delay to allow the camera to start (1-second delay)
time.sleep(1)

# Variable to store very first frame as reference frame
first_frame = None

# List to store status for motion detection
status_list = []

# Counter for saved images
count = 1

# Infinite loop to continuously capture and display video frames
while True:
    # Initialize status for motion detection
    status = 0

    # Read a frame from the video capture object
    check, frame = video.read()

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale frame
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # Check for the first frame to set the reference frame
    if first_frame is None:
        first_frame = gray_frame_gau

    # Calculate the absolute difference between the current frame and the
    # reference frame
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    # Apply thresholding to the difference frame
    thresh_frame = cv2.threshold(delta_frame, 65, 255, cv2.THRESH_BINARY)[1]

    # Dilate the threshold frame to better identify moving objects
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # Find contours of objects in the dilated frame
    contours, check = cv2.findContours(dil_frame,
                                       cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through identified contours
    for contour in contours:
        # Ignore small contours (noise)
        if cv2.contourArea(contour) < 5000:
            continue

        # Get the bounding box coordinates and draw a rectangle around
        # detected objects
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame,
                                  (x, y),
                                  (x + w, y + h),
                                  (0, 255, 0),
                                  3)

        # Save images with detected objects
        if rectangle.any:
            status = 1
            cv2.imwrite(f"images/{count}.png", frame)
            count = count + 1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images) / 2)
            image_with_object = all_images[index]

    # Append current status to the status list
    status_list.append(status)
    status_list = status_list[-2:]

    # Check for status change to trigger an email
    if status_list[0] == 1 and status_list[1] == 0:
        send_email()

    # Display the captured frame in a window titled "My Video"
    cv2.imshow("My Video", frame)

    # Wait for a key press
    key = cv2.waitKey(1)

    # Break the loop if the 'q' key is pressed
    if key == ord("q"):
        break

# Release the video capture object
video.release()
