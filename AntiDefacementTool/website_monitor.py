import difflib
import time
import requests
from config import WEBSITE_URL, CHECK_INTERVAL
from email_alert import send_alert
from sms_alert import send_sms_alert  # Import SMS function from sms_config

# Global Variables
original_content = None  # Stores the initial content of the website
monitoring_active = False  # Flag to control monitoring loop

def fetch_website_content():
    """ Fetches the website content. """
    if WEBSITE_URL.startswith("file:///"):  # Local file monitoring
        try:
            file_path = WEBSITE_URL.replace("file:///", "")  
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            print(f"❌ Error reading local file: {e}")
            return None
    else:  # Online website monitoring
        try:
            response = requests.get(WEBSITE_URL, timeout=5)  # Timeout to prevent hanging
            return response.text if response.status_code == 200 else None
        except requests.RequestException as e:
            print(f"❌ Failed to fetch website content: {e}")
            return None

def check_for_defacement():
    """ Checks if the website content has changed and identifies modifications. """
    global original_content
    current_content = fetch_website_content()

    if current_content is None:
        print("❌ Could not retrieve website content.")
        return

    if original_content is None:
        original_content = current_content
        print("✅ Baseline content saved.")
        return

    if current_content != original_content:
        print("⚠️ Website content has changed! Possible defacement detected.")

        # Identify changes between original and modified content
        diff = difflib.ndiff(original_content.splitlines(), current_content.splitlines())
        changes = "\n".join([line for line in diff if line.startswith("+ ") or line.startswith("- ")])

        # Send alerts and log errors if any
        try:
            send_alert(changes)  # Email Alert
            print("📧 Email alert sent successfully.")
        except Exception as e:
            print(f"❌ Failed to send email alert: {e}")

        try:
            send_sms_alert(changes)  # SMS Alert
            print("📲 SMS alert sent successfully.")
        except Exception as e:
            print(f"❌ Failed to send SMS alert: {e}")

        # Update the stored original content
        original_content = current_content
    else:
        print("✅ Website content unchanged.")

def start_website_monitor():
    """ Starts monitoring in a loop. """
    global original_content, monitoring_active
    monitoring_active = True

    print("🔍 Monitoring started...")
    original_content = fetch_website_content()  # Initialize baseline content

    while monitoring_active:
        check_for_defacement()
        time.sleep(CHECK_INTERVAL)

    print("🛑 Monitoring stopped.")

def stop_website_monitor():
    """ Stops the website monitoring process. """
    global monitoring_active
    monitoring_active = False
    print("🛑 Website monitoring stopped manually.")
