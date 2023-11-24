import smtplib
import os
import imghdr
from dotenv import load_dotenv
from email.message import EmailMessage

# Load app password and email address from environment variables
load_dotenv()
PASSWORD = os.getenv("PASSWORD")
SENDER = os.getenv("EMAIL")
RECEIVER = os.getenv("EMAIL")


# Function to send an email using Gmail SMTP along with an attached image
def send_email(image_path):
    """
    Sends an email with an attached image using Gmail SMTP.

    :param image_path: Path to the image file to be attached.

    This function establishes a connection to Gmail's SMTP server,
    attaches the specified image to the email, and sends it to the
    recipient's email address. It uses environment variables for
    the sender's email and password.
    """

    # Create an EmailMessage object
    email_message = EmailMessage()
    email_message["Subject"] = "New Object Detected"
    email_message.set_content("Hey, A new object just appeared!")

    # Read the image file as binary data and attach it to the email
    with open(image_path, "rb") as file:
        content = file.read()

    # Add the image as an attachment to the email
    email_message.add_attachment(content,
                                 maintype="image",
                                 subtype=imghdr.what(None, content))

    # Establish a connection to Gmail SMTP server and send the email
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
