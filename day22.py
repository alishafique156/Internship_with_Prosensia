Here's the Python code for a simple contact book:

```python
def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print("Contact already exists.")
            return
    contacts.append((name, phone))
    print(f"Contact {name} added.")

def search_contact(contacts):
    name = input("Enter the name to search: ").strip()
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print(f"Found: {contact[0]}, Phone: {contact[1]}")
            return
    print("Contact not found.")

def display_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("Contact List:")
        for contact in contacts:
            print(f"Name: {contact[0]}, Phone: {contact[1]}")

def main():
    contacts = []
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. View All Contacts")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            display_contacts(contacts)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")

main()
