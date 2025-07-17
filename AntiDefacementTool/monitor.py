import os
import hashlib
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import config
import smtplib

class FileMonitorHandler(FileSystemEventHandler):
    def __init__(self):
        self.file_hashes = {}

    def calculate_hash(self, file_path):
        """Calculate SHA-256 hash of a file."""
        try:
            with open(file_path, 'rb') as f:
                return hashlib.sha256(f.read()).hexdigest()
        except Exception as e:
            return None

    def on_modified(self, event):
        """Detect file modification."""
        if event.is_directory:
            return
        file_hash = self.calculate_hash(event.src_path)
        if event.src_path in self.file_hashes and self.file_hashes[event.src_path] != file_hash:
            print(f"⚠️ WARNING: File Modified: {event.src_path}")
            send_email_alert(f"File Modified: {event.src_path}")
        self.file_hashes[event.src_path] = file_hash

def send_email_alert(message):
    """Send an email alert on file modification."""
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(config.EMAIL_SENDER, config.EMAIL_PASSWORD)
        server.sendmail(config.EMAIL_SENDER, config.EMAIL_RECEIVER, f"Subject: Website Defacement Alert\n\n{message}")
        server.quit()
        print("📧 Email alert sent!")
    except Exception as e:
        print("❌ Email sending failed:", e)

def start_file_monitor():
    """Start monitoring the specified directory."""
    if not os.path.exists(config.MONITOR_DIR):
        os.makedirs(config.MONITOR_DIR)

    event_handler = FileMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, config.MONITOR_DIR, recursive=True)
    observer.start()
    print(f"🔍 Monitoring started on {config.MONITOR_DIR}...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
