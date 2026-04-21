

import os
import csv
import sys

CONTACTS_FILE = "contacts.txt"
FIELDS = ["Name", "Phone", "Email", "Address"]

def load_contacts():
    """Load all contacts from the CSV file."""
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def save_contacts(contacts):
    """Save the full contacts list back to the CSV file."""
    with open(CONTACTS_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(contacts)

def print_separator(char="─", width=60):
    print(char * width)


def print_contact(contact, index=None):
    print_separator()
    if index is not None:
        print(f"  Contact #{index}")
        print_separator()
    for field in FIELDS:
        value = contact.get(field, "").strip()
        print(f"  {field:<10}: {value if value else '—'}")
    print_separator()


def print_contacts(contacts, title="Contacts"):
    if not contacts:
        print("\n  No contacts found.\n")
        return
    print(f"\n  {title} ({len(contacts)} found)")
    for i, c in enumerate(contacts, 1):
        print_contact(c, index=i)


def banner():
    print_separator("═")
    print("  📒  CONTACT BOOK APPLICATION")
    print_separator("═")


def menu():
    print("\n  Main Menu")
    print_separator()
    print("  [1] Add Contact")
    print("  [2] View All Contacts")
    print("  [3] Search Contacts")
    print("  [4] Edit Contact")
    print("  [5] Delete Contact")
    print("  [6] Exit")
    print_separator()


def prompt(label, required=False):
    """Prompt the user for input, repeating if required and empty."""
    while True:
        value = input(f"  {label}: ").strip()
        if value or not required:
            return value
        print("  ⚠  This field is required. Please enter a value.")


def pick_contact(contacts):
    """Let the user pick a contact by number. Returns the contact dict or None."""
    print_contacts(contacts)
    if not contacts:
        return None, None
    while True:
        choice = input("  Enter contact number (or 0 to cancel): ").strip()
        if choice == "0":
            return None, None
        if choice.isdigit() and 1 <= int(choice) <= len(contacts):
            idx = int(choice) - 1
            return contacts[idx], idx
        print("  ⚠  Invalid number. Try again.")

def add_contact():
    print("\n  ── Add New Contact ──")
    name = prompt("Name (required)", required=True)

    # Duplicate check
    contacts = load_contacts()
    for c in contacts:
        if c["Name"].lower() == name.lower():
            print(f"\n  ⚠  A contact named '{name}' already exists.")
            overwrite = input("  Add anyway? (y/n): ").strip().lower()
            if overwrite != "y":
                print("  Cancelled.")
                return

    phone   = prompt("Phone")
    email   = prompt("Email")
    address = prompt("Address")

    new_contact = {
        "Name":    name,
        "Phone":   phone,
        "Email":   email,
        "Address": address,
    }
    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"\n  ✅  Contact '{name}' added successfully!")


def view_contacts():
    print("\n  ── All Contacts ──")
    contacts = load_contacts()
    if not contacts:
        print("\n  No contacts stored yet.\n")
        return
    contacts_sorted = sorted(contacts, key=lambda c: c["Name"].lower())
    print_contacts(contacts_sorted, title="All Contacts")


def search_contacts():
    print("\n  ── Search Contacts ──")
    query = prompt("Enter name, phone, or email to search").lower()
    if not query:
        print("  No search term entered.")
        return

    contacts = load_contacts()
    results = [
        c for c in contacts
        if query in c["Name"].lower()
        or query in c["Phone"].lower()
        or query in c["Email"].lower()
        or query in c["Address"].lower()
    ]
    print_contacts(results, title=f"Results for '{query}'")


def edit_contact():
    print("\n  ── Edit Contact ──")
    contacts = load_contacts()
    contact, idx = pick_contact(contacts)
    if contact is None:
        return

    print("\n  Leave a field blank to keep the current value.\n")
    for field in FIELDS:
        if field == "Name":
            # Name is required — show current and keep if blank
            new_val = input(f"  Name [{contact['Name']}]: ").strip()
            if new_val:
                contact["Name"] = new_val
        else:
            current = contact.get(field, "")
            display  = current if current else "—"
            new_val  = input(f"  {field} [{display}]: ").strip()
            if new_val:
                contact[field] = new_val

    contacts[idx] = contact
    save_contacts(contacts)
    print(f"\n  ✅  Contact updated successfully!")


def delete_contact():
    print("\n  ── Delete Contact ──")
    contacts = load_contacts()
    contact, idx = pick_contact(contacts)
    if contact is None:
        return

    confirm = input(f"\n  Delete '{contact['Name']}'? This cannot be undone. (y/n): ").strip().lower()
    if confirm == "y":
        contacts.pop(idx)
        save_contacts(contacts)
        print(f"\n  ✅  Contact '{contact['Name']}' deleted.")
    else:
        print("  Cancelled.")
def main():
    banner()
    print(f"  Data file : {os.path.abspath(CONTACTS_FILE)}")

    actions = {
        "1": add_contact,
        "2": view_contacts,
        "3": search_contacts,
        "4": edit_contact,
        "5": delete_contact,
    }

    while True:
        menu()
        choice = input("  Choose an option [1-6]: ").strip()

        if choice in actions:
            actions[choice]()
        elif choice == "6":
            print("\n  Goodbye! 👋\n")
            sys.exit(0)
        else:
            print("  ⚠  Invalid option. Please choose 1–6.")


if __name__ == "__main__":
    main()
