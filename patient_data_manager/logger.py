from datetime import datetime

LOG_FILE = "error_report.txt"

def log_error(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")
