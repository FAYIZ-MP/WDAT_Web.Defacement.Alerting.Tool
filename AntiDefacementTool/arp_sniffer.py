import requests
import hashlib
import time
import json
from scapy.all import ARP, sniff

# Website URL to monitor
URL = "C:/Users/fayiz/Desktop/MINI04/AntiDefacementTool/website_files/index.html"

# Get initial website content
def get_website_content(url):
    try:
        response = requests.get(url)
        return response.text  # Get website HTML content
    except requests.RequestException:
        return None

# Generate a hash of the website content
def get_hash(content):
    return hashlib.md5(content.encode()).hexdigest()

# Get attacker's public IP
def get_attacker_ip():
    try:
        ip_info = requests.get("https://api64.ipify.org?format=json").json()
        return ip_info["ip"]
    except:
        return "Unknown"

# Capture attacker's MAC address (on the local network)
attacker_mac = "Unknown"
def get_mac(pkt):
    global attacker_mac
    if ARP in pkt and pkt[ARP].op in (1, 2):  # ARP request or reply
        attacker_mac = pkt[ARP].hwsrc  # Extract attacker's MAC address

# Start sniffing ARP packets in a separate thread
from threading import Thread
sniff_thread = Thread(target=lambda: sniff(filter="arp", prn=get_mac, store=0, count=1))
sniff_thread.start()

# Initialize baseline content
original_content = get_website_content(URL)
if original_content:
    original_hash = get_hash(original_content)
else:
    print("Error fetching website content.")
    exit()

print("[INFO] Monitoring started for:", URL)

# Start monitoring loop
while True:
    time.sleep(5)  # Check every 5 seconds
    
    current_content = get_website_content(URL)
    if not current_content:
        continue
    
    current_hash = get_hash(current_content)

    if current_hash != original_hash:  # Detected change
        attacker_ip = get_attacker_ip()
        
        print(f"[ALERT] Website Defacement Detected!\nAttacker IP: {attacker_ip}\nAttacker MAC: {attacker_mac}")

        # Save log
        log_entry = {
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "alert": "Website Defacement Detected",
            "attacker_ip": attacker_ip,
            "attacker_mac": attacker_mac
        }
        with open("defacement_log.json", "a") as log_file:
            json.dump(log_entry, log_file)
            log_file.write("\n")

        # Optional: Send an SMS alert using Twilio or another service

        break  # Stop monitoring after detecting an attack
