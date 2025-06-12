import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for name, info in contacts.items():
        print(f"- {name}: Phone = {info['phone']}, Email = {info['email']}")
    print()

def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    print(f"Editing contact '{name}'...")
    phone = input(f"Enter new phone number (leave blank to keep '{contacts[name]['phone']}'): ").strip()
    email = input(f"Enter new email (leave blank to keep '{contacts[name]['email']}'): ").strip()
    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    print(f"Contact '{name}' updated successfully.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save and Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
