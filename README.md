<img width="3148" height="3148" alt="WDAT LOGO" src="https://github.com/user-attachments/assets/f511d2bb-4910-45fc-97ac-68fab004e967" />
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

🖼️ **Visual Workflow:**  


https://github.com/user-attachments/assets/8572a32e-c363-48f1-aad5-920a4b59a17c

<img width="1919" height="1004" alt="Screenshot 2025-04-04 215026" src="https://github.com/user-attachments/assets/76c27f28-891d-4c48-b3d0-a25fa694754f" />

<img width="1919" height="1004" alt="Screenshot 2025-04-04 215054" src="https://github.com/user-attachments/assets/29e0d465-931a-403e-b52e-cd8fb623698e" />


https://github.com/user-attachments/assets/cbd7507b-7779-4799-91c9-f908a1860443


<img width="1919" height="1003" alt="Screenshot 2025-04-04 215241" src="https://github.com/user-attachments/assets/72daf3ac-c705-45e8-bef8-45e32633d07c" />

![WhatsApp Image 2025-04-08 at 1 24 15 PM (1)](https://github.com/user-attachments/assets/a74356bf-7920-4b26-804a-b3d850b26b5b)

![WhatsApp Image 2025-04-08 at 1 24 15 PM](https://github.com/user-attachments/assets/43330df3-c4fe-49ad-b35f-74c7b2ca3400)

![WDAT OFFICIAL PAGE](https://github.com/user-attachments/assets/b8eaaaf0-3422-41fd-8200-1394d051f4ed)

<img width="1536" height="1024" alt="IMG20252689495404" src="https://github.com/user-attachments/assets/8889ca09-1ad1-469b-bd7e-ed707f0c752d" />

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
