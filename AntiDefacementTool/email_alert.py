import smtplib
from email.mime.text import MIMEText  # ✅ Handles HTML email content
from email.mime.multipart import MIMEMultipart  # ✅ Allows multi-part emails
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER

def send_alert(changes):
    """ Sends an HTML email alert with details of the detected changes. """

    # Email content without embedded image
    message_body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
        <h2 style="color: red;">🚨 Website Defacement Alert! </h2>
        <p><strong>Changes Detected:</strong></p>
        <p><strong>Apple iPhone 15 Pro (256 GB) - Blue Titanium Price has been Modified! 🚨</strong></p>
        <p><strong>Suspect IP Address : 192.168.1.1 </strong></p>
        <div style="background: #fff3cd; padding: 10px; border-left: 5px solid red;">
            <pre style="font-size: 14px; color: #333;">{changes}</pre>
        </div>
        <p><strong>🔍 Please check the website immediately!</strong></p>
    </body>
    </html>
    """

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
