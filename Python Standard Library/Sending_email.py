from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from os import path
from pathlib import Path
import smtplib

message = MIMEMultipart()
message["from"] = "ayush vanparia"
message["to"] = "test1@gmail.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))
message.attach(MIMEImage(Path("1.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("test2@gmail.com", "qwer")
    smtp.send_message(message)
    print("sent...")
