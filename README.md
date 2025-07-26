# 🔍 Wi-Fi Scanner for Open Networks (Windows)

This Python-based tool scans and displays nearby Wi-Fi networks using the Windows `netsh` command. It highlights **open/unsecured** networks that may pose a risk if used without protection.


---

## ✅ Features

- 🔍 Scans nearby Wi-Fi networks via command line.
- 🧠 Detects and lists **SSID** and **Authentication type**.
- 🚨 Marks **open (unsecured)** Wi-Fi networks.
- 💻 Designed specifically for **Windows OS**.

---

## 📸 Sample Output




<img width="513" height="175" alt="Screenshot 2025-07-26 201232" src="https://github.com/user-attachments/assets/45e76bbb-e2e6-4fe3-876c-f7c84ac15221" />









---

## 🛠️ How to Run

### 🧑‍💻 Prerequisites

- OS: Windows 10/11
- Python 3.x installed

### ▶️ Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Rakesh2092004/wifi-scanner.git
   cd wifi-scanner
2.  Run the script:
   ```bash
   python wifi_scanner.py
   ```

## 📄 Code Overview

The script uses Python’s `subprocess` module to run:

```bash
netsh wlan show networks mode=Bssid

```
### ⚠️ Disclaimer
This project is for educational and ethical purposes only.
Please do not misuse the tool to connect or interact with Wi-Fi networks you don’t own or have permission to access.
