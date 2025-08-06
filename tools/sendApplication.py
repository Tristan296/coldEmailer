import pandas as pd
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

from generate import generate_email

# Load jobs CSV
jobs_df = pd.read_csv("results/jobs.csv")

# Email credentials - set these as environment variables for safety
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')  # your email here
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')  # app password or your email password here

# SMTP config for Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  # SSL port

def send_email(to_email, subject, body):
    message = MIMEMultipart()
    message['From'] = EMAIL_ADDRESS
    message['To'] = to_email
    message['Subject'] = subject

    message.attach(MIMEText(body, "plain"))

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_email, message.as_string())

# Example sending to first 5 jobs - update with actual recipient email addresses if known
for idx, job in jobs_df.head(5).iterrows():
    subject, body = generate_email(job)
    recipient_email = job.get('email')  # Make sure your CSV includes recruiter or job poster email
    if recipient_email:
        try:
            send_email(recipient_email, subject, body)
            print(f"Email sent to {recipient_email} for job {job.get('title')}")
        except Exception as e:
            print(f"Failed to send email to {recipient_email}: {e}")
    else:
        print(f"No recipient email found for job: {job.get('title')}")

