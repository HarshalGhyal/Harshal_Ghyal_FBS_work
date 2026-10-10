# Python Assignment – (Pickling and Unpickling)
# 1. Create a class Emp (eid,ename,basic)
# 2. WAP a menu driven program to perform following operations using
# files :

# a. Add a record
# b. Search for a record using id
# c. Delete a record using id
# d. Edit a record using id.
# e. Display all records.

# pickling = python object store into file 
# unpickling = file convert into python object 

from emp import Emp, load_records, save_records


# ---------- Operations ----------

def add_record():
    eid = int(input("Enter Employee ID: "))
    records = load_records()

    # Duplicate check
    for rec in records:
        if rec.eid == eid:
            print("Record with this ID already exists!")
            return

    ename = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    emp = Emp(eid, ename, basic)
    records.append(emp)
    save_records(records)
    print("Record added successfully.")


def search_record():
    eid = int(input("Enter Employee ID to search: "))
    records = load_records()

    for rec in records:
        if rec.eid == eid:
            print("Record found:", rec)
            return
    print("Record not found.")


def delete_record():
    eid = int(input("Enter Employee ID to delete: "))
    records = load_records()

    new_records = [rec for rec in records if rec.eid != eid]

    if len(new_records) == len(records):
        print("Record not found.")
    else:
        save_records(new_records)
        print("Record deleted successfully.")


def edit_record():
    eid = int(input("Enter Employee ID to edit: "))
    records = load_records()

    for rec in records:
        if rec.eid == eid:
            print("Current record:", rec)
            rec.ename = input("Enter new Name: ")
            rec.basic = float(input("Enter new Basic Salary: "))
            save_records(records)
            print("Record updated successfully.")
            return
    print("Record not found.")


def display_all():
    records = load_records()
    if not records:
        print("No records to display.")
        return
    print("\n--- All Employee Records ---")
    for rec in records:
        print(rec)
    print("----------------------------")


# ---------- Menu ----------

def menu():
    while True:
        print("\n===== Employee Menu =====")
        print("1. Add a record")
        print("2. Search a record")
        print("3. Delete a record")
        print("4. Edit a record")
        print("5. Display all records")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_record()
        elif choice == "2":
            search_record()
        elif choice == "3":
            delete_record()
        elif choice == "4":
            edit_record()
        elif choice == "5":
            display_all()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    menu()