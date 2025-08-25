import json
from add_contact import add_contact
from list_contact import list_contact
from search_contact import search_contact
from exit_contact import exit_contact
# Load contacts from file
try:
    with open("contacts.json", "r") as f:
        a = json.load(f)
except FileNotFoundError:
    a = []

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. List Contacts")
    print("3. Search Contact")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_contact(a)
    elif choice == "2":
        list_contact(a)
    elif choice == "3":
        search_contact(a)
    elif choice == "4":
        # Save contacts before exit
        with open("contacts.json", "w") as f:
            json.dump(a, f)
        exit_contact()
        break
    else:
        print("❌ Invalid choice, try again.")
