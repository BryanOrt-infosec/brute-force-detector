log_file = "logs/auth.log"

failed_attempts = {}

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()
            ip = parts[-1]

            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

print("Brute Force Detection Results")
print("-----------------------------")

for ip, count in failed_attempts.items():
    print(f"{ip}: {count} failed attempts")

    if count >= 3:
        print(f"Potential brute force attack detected from {ip}")
