import tkinter as tk
import threading
import website_monitor
from tkinter import messagebox
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import os

# Global Variables
monitoring_thread = None
monitoring_active = False

def start_web_monitor():
    """ Starts the website monitoring process in a new thread. """
    global monitoring_thread, monitoring_active
    if not monitoring_active:
        monitoring_active = True
        monitoring_thread = threading.Thread(target=website_monitor.start_website_monitor, daemon=True)
        monitoring_thread.start()
        status_label.config(text="Status: Monitoring Active ✅", foreground="#00ff00")
        messagebox.showinfo("Monitoring Started", "Website monitoring is now active!")
    else:
        messagebox.showwarning("Already Running", "Monitoring is already active.")

def stop_web_monitor():
    """ Stops the website monitoring process. """
    global monitoring_active
    if monitoring_active:
        confirmation = messagebox.askyesno("Confirm Stop", "Are you sure you want to stop monitoring?")
        if confirmation:
            monitoring_active = False
            website_monitor.stop_website_monitor()  # Ensure this function is properly defined in website_monitor.py
            status_label.config(text="Status: Monitoring Stopped ❌", foreground="#ff0000")
            messagebox.showinfo("Monitoring Stopped", "Website monitoring has been stopped.")
    else:
        messagebox.showwarning("Not Running", "Monitoring is not active.")

# Create Themed GUI Window
root = ThemedTk(theme="arc")  # A sleek, modern cybersecurity-inspired theme
root.title("WDAT - Web Defacement Monitor")
root.geometry("500x400")
root.configure(bg="#1E1E1E")  # Updated background color (dark grey)

# Load and Display Tool's Logo
logo_path = r"C:\Users\fayiz\Desktop\MINI04\AntiDefacementTool\icon.png"  # Set the correct path

if os.path.exists(logo_path):  
    logo_img = Image.open(logo_path)
else:
    print("⚠️ Warning: icon.png not found! Using default blank logo.")
    logo_img = Image.new("RGB", (80, 80), "black")  # Fallback image

logo_img = logo_img.resize((80, 80), Image.LANCZOS)
logo = ImageTk.PhotoImage(logo_img)
logo_label = tk.Label(root, image=logo, bg="#1E1E1E")  # Updated background color
logo_label.pack(pady=10)

# Title Label
title_label = tk.Label(root, text="Anti-Web Defacement Tool", font=("Orbitron", 16, "bold"), fg="#00ffff", bg="#1E1E1E")
title_label.pack(pady=10)

# Start Monitoring Button (Modern Dark Green)
start_button = tk.Button(root, text="🛠️ Start Monitoring", command=start_web_monitor, font=("Arial", 12, "bold"), 
                         bg="#228B22", fg="#fff", padx=20, pady=10, activebackground="#006400", activeforeground="#fff")
start_button.pack(pady=10)

# Stop Monitoring Button (Professional Red)
stop_button = tk.Button(root, text="🛑 Stop Monitoring", command=stop_web_monitor, font=("Arial", 12, "bold"), 
                        bg="#B22222", fg="#fff", padx=20, pady=10, activebackground="#8B0000", activeforeground="#fff")
stop_button.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="Status: Waiting...", font=("Consolas", 12), fg="#ffcc00", bg="#1E1E1E")
status_label.pack(pady=10)

# Run the main loop
root.mainloop()
