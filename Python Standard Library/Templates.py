from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib


template = Template(
    Path(r"E:\\Devops\Ayush_Vanparia\Python Standard Library\Template.html"))
message = MIMEMultipart()
message["from"] = "ayush vanparia"
message["to"] = "test1@gmail.com"
message["subject"] = "This is a test"
body = template.substitute(name="ayush")
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("1.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("test2@gmail.com", "qwer")
    smtp.send_message(message)
    print("sent...")
