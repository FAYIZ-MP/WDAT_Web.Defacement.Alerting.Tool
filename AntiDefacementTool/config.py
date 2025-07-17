import os

# Directory to monitor
MONITOR_DIR = "./website_files"

# Webpage URL to monitor (Use file:// for local files)
WEBSITE_URL = "file:///" + os.path.abspath("C:/Users/fayiz/Desktop/MINI04/AntiDefacementTool/website_files/index.html")

# Email notification settings
EMAIL_SENDER = "tool engine's email address"
EMAIL_PASSWORD = "tool engine's email password"  # Use Gmail App Password
EMAIL_RECEIVER = "admin's email address"


# Monitoring interval in seconds
CHECK_INTERVAL = 30
