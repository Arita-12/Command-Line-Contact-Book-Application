# 📒 Command-Line Contact Book

A lightweight, fully offline contact manager that runs in your terminal and stores all data in a plain-text CSV file — no database, no dependencies, just Python.

---

## Features

- **Add** contacts with name, phone, email, and address
- **View** all contacts sorted alphabetically
- **Search** across every field (name, phone, email, address)
- **Edit** any field of an existing contact
- **Delete** contacts with a confirmation prompt
- **Duplicate detection** — warns before adding a contact with the same name
- Data stored in a human-readable `contacts.txt` CSV file

---

## Requirements

- Python 3.6 or higher
- No external libraries — uses only the Python standard library

---

## Installation

1. Download or clone the file:

   ```bash
   git clone https://github.com/your-username/contact-book.git
   cd contact-book
   ```

   Or simply download `contact_book.py` directly.

2. No installation step needed — just run it.

---

## Usage

### On Windows

```powershell
python contact_book.py
```

### On macOS / Linux

```bash
python3 contact_book.py
```

### Main Menu

```
════════════════════════════════════════════════════════════
  📒  CONTACT BOOK APPLICATION
════════════════════════════════════════════════════════════
  Data file : /your/path/contacts.txt

  Main Menu
────────────────────────────────────────────────────────────
  [1] Add Contact
  [2] View All Contacts
  [3] Search Contacts
  [4] Edit Contact
  [5] Delete Contact
  [6] Exit
────────────────────────────────────────────────────────────
```

---

## Menu Options

| Option | Description |
|--------|-------------|
| **1 – Add Contact** | Enter name (required), phone, email, and address. Warns if a contact with the same name exists. |
| **2 – View All Contacts** | Displays all saved contacts sorted alphabetically by name. |
| **3 – Search Contacts** | Case-insensitive search across name, phone, email, and address fields. |
| **4 – Edit Contact** | Select a contact by number and update any field. Leave a field blank to keep the existing value. |
| **5 – Delete Contact** | Select a contact and confirm deletion. This action cannot be undone. |
| **6 – Exit** | Exits the application. |

---

## Data Storage

All contacts are saved locally in a file called **`contacts.txt`** in the same directory as the script. It uses standard CSV format and can be opened in any text editor or spreadsheet application (Excel, Google Sheets, etc.).

**Example `contacts.txt`:**

```
Name,Phone,Email,Address
Alice Smith,9876543210,alice@email.com,123 Main St
Bob Jones,1234567890,bob@email.com,456 Oak Ave
```

> **Tip:** You can manually edit `contacts.txt` in a text editor or spreadsheet app — just keep the header row intact.

---

## Example Session

```
  ── Add New Contact ──
  Name (required): Jane Doe
  Phone: 555-0101
  Email: jane@example.com
  Address: 789 Elm Street

  ✅  Contact 'Jane Doe' added successfully!

  ── Search Contacts ──
  Enter name, phone, or email to search: jane

  Results for 'jane' (1 found)
────────────────────────────────────────────────────────────
  Contact #1
────────────────────────────────────────────────────────────
  Name      : Jane Doe
  Phone     : 555-0101
  Email     : jane@example.com
  Address   : 789 Elm Street
────────────────────────────────────────────────────────────
```

---

## Project Structure

```
contact-book/
├── contact_book.py   # Main application script
├── contacts.txt      # Auto-created on first contact added
└── README.md         # This file
```

---

## Troubleshooting

**`python` is not recognized (Windows)**
- Reinstall Python from [python.org](https://www.python.org/downloads/) and check **"Add Python to PATH"** during setup.
- Or try `py contact_book.py` instead.

**`/usr/bin/env` error in PowerShell**
- Don't run the file path directly in PowerShell. Use `python contact_book.py` instead.

**`contacts.txt` is missing**
- The file is created automatically the first time you add a contact. This is normal.

---


