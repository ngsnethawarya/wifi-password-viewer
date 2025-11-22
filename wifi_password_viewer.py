import subprocess
import re

def get_saved_wifi_profiles():
    cmd = ["netsh", "wlan", "show", "profiles"]
    output = subprocess.check_output(cmd).decode(errors="ignore")
    profiles = re.findall(r"All User Profile\s*: (.*)", output)
    return [p.strip() for p in profiles]

def get_wifi_password(profile):
    cmd = ["netsh", "wlan", "show", "profile", profile, "key=clear"]
    output = subprocess.check_output(cmd).decode(errors="ignore")
    password = re.search(r"Key Content\s*: (.*)", output)
    return password.group(1).strip() if password else "N/A"

def main():
    print("\n==== Saved Wi-Fi Networks & Passwords ====\n")
    profiles = get_saved_wifi_profiles()

    if not profiles:
        print("No Wi-Fi profiles found.")
        return

    for p in profiles:
        password = get_wifi_password(p)
        print(f"{p} : {password}")

if __name__ == "__main__":
    main()
