# What is this project?

This application continuously monitors the webcam feed for any detected movement and sends an email alert when motion is detected.

## Features

- **Motion Detection**: Using the webcam feed, the application detects motion by comparing frames and identifies changes.
- **Email Alert**: When motion is detected, the app sends an email alert with an image showing the detected motion.
- **Image Storage**: Captured images of detected motion are saved locally for reference and later gets deleted once the email has been sent.

## File Structure

- `main.py`: Main script for webcam monitoring and motion detection.
- `send_email.py`: Handles the sending of email alerts.
- `images/`: Directory for storing captured images of detected motion.
- `requirements.txt`: Contains the necessary Python libraries.
