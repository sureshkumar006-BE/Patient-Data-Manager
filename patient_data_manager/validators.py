import re
from datetime import datetime

VALID_DIAGNOSIS = [
    "Hypertension", "Diabetes", "Asthma",
    "Migraine", "Arthritis", "Other"
]

def validate_patient_id(pid):
    return bool(re.fullmatch(r"P\d{3}", pid))

def validate_name(name):
    return bool(re.fullmatch(r"[A-Za-z ]{2,50}", name))

def validate_age(age):
    return age.isdigit() and 0 <= int(age) <= 120

def validate_diagnosis(diagnosis):
    return diagnosis in VALID_DIAGNOSIS

def validate_date(date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        return date <= datetime.now()
    except ValueError:
        return False
