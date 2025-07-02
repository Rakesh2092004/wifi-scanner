import subprocess

print("Scanning nearby Wi-Fi networks...\n")

result = subprocess.check_output(["netsh", "wlan", "show", "networks", "mode=Bssid"], shell=True)
output = result.decode("utf-8", errors="ignore").split("\n")

networks = []
for line in output:
    line = line.strip()
    if line.startswith("SSID"):
        ssid = line.split(":", 1)[1].strip()
    if line.startswith("Authentication"):
        auth = line.split(":", 1)[1].strip()
        networks.append((ssid, auth))

print("Found Networks:")
for i, (ssid, auth) in enumerate(networks, start=1):
    if auth.lower() == "open":
        print(f"{i}. {ssid} – 🔓 Open (Unsecure)")
    else:
        print(f"{i}. {ssid} – 🔐 Secured")
