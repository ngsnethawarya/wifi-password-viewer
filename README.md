#  WiFi Password Viewer (Windows)

A simple Python script that retrieves and displays **saved Wi-Fi passwords** on Windows using the built-in `netsh` command.

---

##  Legal & Ethical Warning

This tool is for **educational and personal use only**.  
You may only view passwords for **networks you own** or have explicit permission to access.

Unauthorized access to networks is illegal under **U.S. CFAA** and **international cybersecurity laws**.

---

##  How It Works

Windows stores Wi-Fi profiles locally.  
This script uses:

```bash
netsh wlan show profiles
netsh wlan show profile "<name>" key=clear
