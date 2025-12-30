from validators import *
from logger import log_error
from file_handler import load_csv, save_csv

class PatientManager:

    def __init__(self):
        self.patients = []
        self.load_data()

    def load_data(self):
        rows = load_csv("patients.csv")
        for row in rows:
            errors = self.validate_patient(row)
            if errors:
                for err in errors:
                    log_error(err)
            else:
                self.patients.append(row)
        save_csv("valid_patients.csv", self.patients)

    def validate_patient(self, p):
        errors = []
        if not validate_patient_id(p["patient_id"]):
            errors.append(f"Invalid Patient ID: {p}")
        if not validate_name(p["name"]):
            errors.append(f"Invalid Name: {p}")
        if not validate_age(p["age"]):
            errors.append(f"Invalid Age: {p}")
        if not validate_diagnosis(p["diagnosis"]):
            errors.append(f"Invalid Diagnosis: {p}")
        if not validate_date(p["admission_date"]):
            errors.append(f"Invalid Date: {p}")
        return errors

    def add_patient(self):
        p = {
            "patient_id": input("Patient ID: "),
            "name": input("Name: "),
            "age": input("Age: "),
            "diagnosis": input("Diagnosis: "),
            "admission_date": input("Admission Date (YYYY-MM-DD): ")
        }
        errors = self.validate_patient(p)
        if errors:
            print("Errors:")
            for e in errors:
                print(e)
                log_error(e)
        else:
            self.patients.append(p)
            save_csv("valid_patients.csv", self.patients)
            print("Patient added")

    def view_patients(self):
        for p in self.patients:
            print(p)

    def search_patient(self):
        pid = input("Patient ID: ")
        for p in self.patients:
            if p["patient_id"] == pid:
                print(p)
                return
        print("Patient not found")

    def update_patient(self):
        pid = input("Patient ID: ")
        for p in self.patients:
            if p["patient_id"] == pid:
                p["name"] = input("New Name: ")
                p["age"] = input("New Age: ")
                p["diagnosis"] = input("New Diagnosis: ")
                p["admission_date"] = input("New Date: ")
                save_csv("valid_patients.csv", self.patients)
                print("Updated")
                return
        print("Patient not found")

    def delete_patient(self):
        pid = input("Patient ID: ")
        self.patients = [p for p in self.patients if p["patient_id"] != pid]
        save_csv("valid_patients.csv", self.patients)
        print("Deleted")
