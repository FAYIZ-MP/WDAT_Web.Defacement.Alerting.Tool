import smtplib
from email.mime.text import MIMEText  # ✅ Handles HTML email content
from email.mime.multipart import MIMEMultipart  # ✅ Allows multi-part emails
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER

def send_alert(changes):
    """ Sends an HTML email alert with details of the detected changes. """


    msg = MIMEMultipart()
    msg["Subject"] = "🚨 ALERT: Website Defacement Detected!"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    # Attach HTML content
    msg.attach(MIMEText(message_body, "html"))

    # Send the email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        print("📧 HTML Alert email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
