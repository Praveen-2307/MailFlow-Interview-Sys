import os

def send_email(to_email, subject, body):
    if os.getenv("ENV") == "production":
        # TODO: Replace with real email provider code (SendGrid, SMTP, etc.)
        print(f"Sending REAL email to {to_email} with subject {subject}")
    else:
        # Development mode - just print email contents
        print(f"[DEV] Sending email to {to_email}")
        print(f"Subject: {subject}")
        print(f"Body:\n{body}")

