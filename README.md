
# 🛡️ WDAT - Web Defacement Alerting Tool

## 🔍 Overview

**WDAT (Web Defacement Alerting Tool)** is a **real-time cybersecurity solution** designed to detect unauthorized website modifications (defacements) and trigger **instant alerts via Email and SMS**.

This tool protects **e-commerce websites, corporate portals, and critical online assets** from defacement attacks that could lead to reputation damage, fraud, or business disruption.

---

## 💻 How WDAT Works

### 📟Overall Workflow:

1️⃣ **Website Monitoring**  
WDAT continuously monitors the target website's content, including text, images, and product details.

2️⃣ **Defacement Attempt**  
When an attacker changes a price, product image, or text, WDAT detects the modification.

3️⃣ **Real-Time Detection**  
WDAT instantly compares the **original content** with the **modified version** using advanced diff algorithms.

4️⃣ **Instant Alerts**  
- 📧 **Email Alert:** Sent with detailed change logs  
- 📲 **SMS Alert:** Sent via Twilio API  
- 🔗 **Attacker Trace:** IP and MAC address are logged (via ARP sniffing and public IP lookup)

5️⃣ **Admin Action Panel**  
Admins receive the alert and can respond immediately through the WDAT GUI dashboard. Features include **freezing the website temporarily** or logging the event for investigation.

---

## 🧩 Key Features

| Feature | Description |
|----------|-------------|
| 🖥️ Website Content Monitoring | Detects real-time changes in HTML, text, or images |
| 🔗 ARP & IP Sniffing | Captures attacker’s MAC and public IP |
| 📧 Email Notifications | Sends HTML-formatted alerts with change details |
| 📲 SMS Alerts | Uses Twilio API for real-time SMS alerts |
| 🛡️ GUI Dashboard | Tkinter-based interface for start/stop control |
| 🗂️ JSON Logging | Logs incidents for forensic analysis |

---

## 📂 Project Structure

```
├── main.py                # GUI Control Panel
├── website_monitor.py     # Core monitoring logic
├── email_alert.py         # Sends Email Alerts
├── sms_alert.py           # Sends SMS Alerts via Twilio
├── arp_sniffer.py         # Captures MAC Address using Scapy
├── monitor.py              # Optional filesystem monitoring
├── config.py               # Email, URL, and interval configs
├── sms_config.py           # Twilio API configs
├── defacement_log.json    # Log file for alerts
├── icon.png                # GUI Icon
└── index.html              # Demo e-commerce website (target page)
```

---

## ⚙️ Tech Stack

- **Python 3.8+**  
- **Scapy** (Network sniffing)  
- **Watchdog** (File monitoring)  
- **Twilio API** (SMS alerts)  
- **SMTP (Gmail)** (Email notifications)  
- **Tkinter + ttkthemes** (GUI)  
- **Difflib** (Change detection)  

---

## 🛠️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/WDAT-Web-Defacement-Tool.git
cd WDAT-Web-Defacement-Tool
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure

- Open `config.py`  
  - Set `WEBSITE_URL`, `EMAIL_SENDER`, `EMAIL_RECEIVER`, and `CHECK_INTERVAL`
- Open `sms_config.py`  
  - Add your **Twilio Account SID, Auth Token, and Phone Numbers**

### 4️⃣ Run the Tool

```bash
python main.py
```

---

## 📊 Demo Preview

🎥 **Video Demo:**  
*(Add your Pika-generated video link here or YouTube link)*

🖼️ **Visual Workflow:**  
![WDAT Workflow](./path_to_your_flowchart.png)

---

## 🔒 Use Cases

- **E-Commerce Defacement Prevention**  
- **Corporate Website Protection**  
- **SOC Monitoring & Alerting Systems**  
- **Cyber Forensics & Network Security Labs**

---

## 📜 License
Licensed under the **MIT License**.

## 👨‍💻 About the Developer
Developed by **Fayiz M P**, a passionate **Cybersecurity Engineer & Developer** focused on creating secure and innovative applications.

☣️ 𝐂𝐲𝐛𝐞𝐫𝐬𝐞𝐜𝐮𝐫𝐢𝐭𝐲 𝐄𝐧𝐭𝐡𝐮𝐬𝐢𝐚𝐬𝐭𝐬 – 𝐋𝐞𝐭’𝐬 𝐂𝐨𝐧𝐧𝐞𝐜𝐭 & 𝐆𝐫𝐨𝐰 𝐓𝐨𝐠𝐞𝐭𝐡𝐞𝐫!🔐

🔗 [LinkedIn]www.linkedin.com/in/fayizmp | [GitHub]https://github.com/FAYIZ-MP
