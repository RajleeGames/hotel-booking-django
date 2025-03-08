import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def get_gmail_token():
    creds = None
    token_path = "token.pickle"

    # Load existing credentials if available
    if os.path(token_path):
        with open(token_path, "rb") as token:
            creds = pickle.load(token)

    # If no valid credentials, go through the OAuth2 flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for future use
        with open(token_path, "wb") as token:
            pickle.dump(creds, token)

    return creds

if __name__ == "__main__":
    get_gmail_token()
    print("OAuth2 token generated and saved as token.pickle!")
