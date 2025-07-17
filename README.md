
# 🚨 **WDAT - Web Defacement Alerting Tool** 🚨

### **"Because Cyber Threats Don't Knock—They Strike."**

---

## 🛡️ **Introduction**

In a digital world where your **website is your brand's face**, defacement attacks can ruin trust in seconds.  
**WDAT (Web Defacement Alerting Tool)** provides **real-time, proactive defense** against such threats, combining **network monitoring**, **web integrity verification**, and **instant alerts**.

Whether it's a **price change in an e-commerce store**, a **logo swap**, or a **malicious message injected into your homepage**—**WDAT catches it first**.

---

## 🎯 **Key Highlights**

### ✅ **Real-Time Monitoring**  
Continuously scans website files or live web pages for unauthorized changes.

### ✅ **Attacker Identification**  
Captures **MAC and IP addresses** of potential intruders via **ARP sniffing & public IP tracing**.

### ✅ **Instant Multi-Channel Alerts**  
- 📧 **Email Alerts** with detailed change logs & timestamps  
- 📲 **SMS Alerts** via Twilio API—direct to your phone

### ✅ **GUI Control Panel**  
A **Tkinter-based dashboard** for starting, stopping, and viewing monitoring status.

### ✅ **Actionable Defense**  
Freeze malicious activity instantly via the GUI panel—**defend in real-time**.

---

## 🔍 **How It Works – Cinematic Workflow**

1️⃣ **🖥️ Monitoring Starts:**  
WDAT monitors your website's content, waiting silently in the background.

2️⃣ **⚠️ Defacement Attempt Detected:**  
A hacker alters a price, image, or text—WDAT detects the change **instantly**.

3️⃣ **🔗 Attacker Traced:**  
WDAT captures the **attacker's IP and MAC address** while comparing content differences.

4️⃣ **🚨 Alerts Triggered:**  
- Email + SMS sent to admins within seconds  
- Logs saved with full forensic details

5️⃣ **🛡️ Admin Response:**  
Use the **GUI dashboard** to freeze actions or investigate further.

---

## 🗂️ **Project Structure**

```
📦 WDAT - Web Defacement Alerting Tool
├── main.py                # GUI Control Panel
├── website_monitor.py     # Core website monitoring
├── email_alert.py         # Email alert system
├── sms_alert.py           # SMS via Twilio
├── arp_sniffer.py         # ARP Sniffing (MAC Detection)
├── monitor.py              # Optional file system monitoring
├── config.py               # Configuration settings
├── sms_config.py           # Twilio API keys and phone numbers
├── defacement_log.json    # Log of defacement incidents
├── icon.png                # GUI icon
└── index.html              # Sample target website
```

---

## ⚙️ **Technology Stack**

| Component | Technology |
|------------|-------------|
| Programming Language | Python 3.8+ |
| GUI Framework | Tkinter + ttkthemes |
| Network Sniffing | Scapy |
| File Monitoring | Watchdog |
| Email Alerts | Gmail SMTP |
| SMS Alerts | Twilio API |
| Diff Comparison | Difflib |
| Logging | JSON |

---

## 🚀 **Installation & Setup**

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/WDAT-Web-Defacement-Tool.git
cd WDAT-Web-Defacement-Tool
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure the Tool

- Open `config.py` for email, website path, and check interval  
- Open `sms_config.py` for Twilio configuration

### 4️⃣ Launch the GUI

```bash
python main.py
```

---

## 📺 **Demo & Preview**

🎥 **Video Demo:** *(Upload your Pika Labs or YouTube link here)*

🖼️ **Visual Workflow:**  
![WDAT Workflow](./path_to_your_flowchart.png)

---

## 🔒 **Use Cases**

- 🛍️ **E-Commerce Website Protection**  
- 📰 **News Portal Integrity Assurance**  
- 🏢 **Corporate Brand Security**  
- 🕵️ **Cyber Forensics & SOC Tools**  

---

## 🤝 **Contribute & Collaborate**

We welcome contributions, feature enhancements, and security ideas!  
Please open a pull request or issue to discuss your suggestions.

---

## 📄 **License**

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## 👤 **Developer Info**

**Fayiz M P**  
📧 Email: fayizmp2003@gmail.com  
🔗 LinkedIn: [Fayiz M P](https://www.linkedin.com/in/fayizmp)

---

## ⭐ **If you find this project valuable, give it a star!**

