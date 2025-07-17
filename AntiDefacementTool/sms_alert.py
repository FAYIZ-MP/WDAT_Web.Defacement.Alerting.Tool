from twilio.rest import Client
from sms_config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, ADMIN_PHONE_NUMBER

def send_sms_alert(message):
    """ Sends an SMS alert using Twilio. """
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        sms = client.messages.create(
            body=f"\n{message}",
            from_=TWILIO_PHONE_NUMBER,
            to=ADMIN_PHONE_NUMBER
        )
        print(f"📲 SMS alert sent! Message SID: {sms.sid}")
    except Exception as e:
        print(f"❌ Failed to send SMS: {e}")
