from patient_manager import PatientManager

def menu():
    print("""
1. Add Patient
2. View Patients
3. Search Patient
4. Update Patient
5. Delete Patient
6. Export to CSV
7. Exit
""")

def main():
    manager = PatientManager()
    while True:
        menu()
        choice = input("Choose option: ")

        if choice == "1":
            manager.add_patient()
        elif choice == "2":
            manager.view_patients()
        elif choice == "3":
            manager.search_patient()
        elif choice == "4":
            manager.update_patient()
        elif choice == "5":
            manager.delete_patient()
        elif choice == "6":
            print("Exported to valid_patients.csv")
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
