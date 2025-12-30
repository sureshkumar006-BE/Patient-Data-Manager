import csv

def load_csv(file_name):
    try:
        with open(file_name, newline="") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []

def save_csv(file_name, data):
    if not data:
        return
    with open(file_name, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
