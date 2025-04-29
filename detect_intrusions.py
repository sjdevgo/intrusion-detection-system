import re
from collections import defaultdict

# Path to your sample log file
log_file_path = 'sample_logs/auth.log'

# Thresholds
FAILED_LOGIN_THRESHOLD = 5
NIGHT_HOURS = range(0, 6)  # 00:00 - 05:59

# Data holders
failed_login_counts = defaultdict(int)
night_logins = []

# Read the log file
with open(log_file_path, 'r') as file:
    for line in file:
        # Check for failed logins
        if 'Failed password' in line:
            ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if ip_match:
                ip = ip_match.group(1)
                failed_login_counts[ip] += 1

        # Check for accepted logins during night hours
        if 'Accepted password' in line:
            time_match = re.search(r'\d{2}:\d{2}:\d{2}', line)
            if time_match:
                time_str = time_match.group(0)
                hour = int(time_str.split(':')[0])
                if hour in NIGHT_HOURS:
                    night_logins.append(line.strip())

# Output suspicious failed logins
print("\n[ALERT] Possible Brute Force Attempts:")
for ip, count in failed_login_counts.items():
    if count >= FAILED_LOGIN_THRESHOLD:
        print(f"IP: {ip} | Failed Attempts: {count}")

# Save alerts to a file
with open('alerts.txt', 'w') as alert_file:
    alert_file.write("[ALERT] Possible Brute Force Attempts:\n")
    for ip, count in failed_login_counts.items():
        if count >= FAILED_LOGIN_THRESHOLD:
            alert_file.write(f"IP: {ip} | Failed Attempts: {count}\n")
    
    alert_file.write("\n[ALERT] Unusual Night-Time Logins:\n")
    for login in night_logins:
        alert_file.write(login + "\n")

print("\nAlerts have been saved to alerts.txt")

