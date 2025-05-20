import tkinter as tk
from tkinter import messagebox
import json

CONTACT_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACT_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts():
    with open(CONTACT_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts()
        messagebox.showinfo("Success", f"Contact '{name}' added!")
        update_contact_list()
    else:
        messagebox.showwarning("Error", "Name and Phone are required!")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name}: {details['Phone']}")

def search_contact():
    query = search_entry.get().lower()
    contact_list.delete(0, tk.END)

    for name, details in contacts.items():
        if query in name.lower() or query in details["Phone"]:
            contact_list.insert(tk.END, f"{name}: {details['Phone']}")

def update_contact():
    selected = contact_list.get(tk.ACTIVE)
    if selected:
        name = selected.split(":")[0].strip()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        if name in contacts:
            contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            save_contacts()
            messagebox.showinfo("Success", f"Contact '{name}' updated!")
            update_contact_list()
        else:
            messagebox.showerror("Error", "Contact not found!")

def delete_contact():
    selected = contact_list.get(tk.ACTIVE)
    if selected:
        name = selected.split(":")[0].strip()
        if name in contacts:
            del contacts[name]
            save_contacts()
            messagebox.showinfo("Success", f"Contact '{name}' deleted!")
            update_contact_list()
        else:
            messagebox.showerror("Error", "Contact not found!")

root = tk.Tk()
root.title("Contact Management System")
root.geometry("400x400")

contacts = load_contacts()

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone:").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Address:").pack()
address_entry = tk.Entry(root)
address_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack()
tk.Button(root, text="Update Contact", command=update_contact).pack()
tk.Button(root, text="Delete Contact", command=delete_contact).pack()

tk.Label(root, text="Search:").pack()
search_entry = tk.Entry(root)
search_entry.pack()
tk.Button(root, text="Search", command=search_contact).pack()

contact_list = tk.Listbox(root, width=50)
contact_list.pack()
update_contact_list()

root.mainloop()
