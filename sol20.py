import csv
import time

# holds all contacts here
contacts = []


def add(contact):
    contact["id"] = time.time()
    contacts.append(contact)


def list_all():
    for contact in contacts:
        print(contact["name"], contact["phone"])


def remove(id):
    _contacts = []
    global contacts
    for contact in contacts:
        if contact["id"] == id:
            _contacts.append(contact)

    contacts = _contacts


def update(id, updated_contact):
    _contacts = []
    global contacts
    for contact in contacts:
        if contact["id"] != id:
            _contacts.append(contact)
        else:
            _contacts.append(updated_contact)

    contacts = _contacts


def id_exists(id):
    for contact in contacts:
        if contact["id"] == id:
            return True
    return False


def save():
    file = open("contacts.csv", "w")
    writer = csv.DictWriter(file, fieldnames=("id", "name", "phone"))
    writer.writeheader()
    for contact in contacts:
        writer.writerow(contact)

    file.close()


def read():
    file = open("contacts.csv", "r")
    lines = 0
    reader = csv.DictReader(file)

    for row in reader:
        if lines == 0:
            print(f'Column names are {", ".join(row)}')
            lines += 1
        contacts.append({
            "id": row["id"],
            "name": row["name"],
            "phone": row["phone"]
        })
        lines += 1

    file.close()


def show_menu():
    print("1. Add")
    print("2. List")
    print("3. Update")
    print("4. Remove")
    print("5. Quit")


quitApp = False
read()

while not quitApp:
    show_menu()

    choice = int(input("Enter choice : "))
    if choice == 1:
        contact = {
            "name": input("Enter name : "),
            "phone": input("Enter phone : ")
        }
        add(contact)

    elif choice == 2:
        list_all()

    elif choice == 3:
        id = int(input("Enter id to update : "))
        if id_exists(id):
            contact = {
                "name": input("Enter new name : "),
                "phone": input("Enter new phone : ")
            }
            update(id, contact)
        else:
            print("no id found")

    elif choice == 4:
        id = int(input("Enter id to remove : "))
        if id_exists(id):
            remove(id)
        else:
            print("no id found")

    elif choice == 5:
        quitApp = True
        save()
