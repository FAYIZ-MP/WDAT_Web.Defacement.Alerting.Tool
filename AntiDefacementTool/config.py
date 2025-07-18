import os

# Directory to monitor
MONITOR_DIR = "./website_files"

# Webpage URL to monitor (Use file:// for local files)
WEBSITE_URL = "file:///" + os.path.abspath("C:/Users/fayiz/Desktop/MINI04/AntiDefacementTool/website_files/index.html")

# Email notification settings
EMAIL_SENDER = "wdat135790@gmail.com"
EMAIL_PASSWORD = "zynqjyhytwaantee"  # Use Gmail App Password
EMAIL_RECEIVER = "fayizmp2003@gmail.com"


# Monitoring interval in seconds
CHECK_INTERVAL = 30
