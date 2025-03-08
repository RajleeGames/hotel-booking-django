import base64
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText
from django.conf import settings

def send_gmail_oauth2(to_email, subject, body):
    """
    Sends an email via the Gmail API using OAuth2 credentials.
    """
    creds = Credentials.from_authorized_user_file(
        settings.EMAIL_OAUTH2_TOKEN_PATH,
        ["https://www.googleapis.com/auth/gmail.send"]
    )
    service = build("gmail", "v1", credentials=creds)

    # Construct the email
    message = MIMEText(body)
    message["to"] = to_email
    message["subject"] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    # Send the email
    send_message = service.users().messages().send(
        userId="me",
        body={"raw": raw_message}
    ).execute()

    return send_message
