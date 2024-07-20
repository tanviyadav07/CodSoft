import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self, root):
        self.contacts = []
        self.root = root
        self.root.title("Contact Book")
        
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Name").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.name_var).grid(row=0, column=1)
        
        tk.Label(self.root, text="Phone").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.phone_var).grid(row=1, column=1)
        
        tk.Label(self.root, text="Email").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.email_var).grid(row=2, column=1)
        
        tk.Label(self.root, text="Address").grid(row=3, column=0)
        tk.Entry(self.root, textvariable=self.address_var).grid(row=3, column=1)
        
        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=5, column=0, columnspan=2)
        tk.Button(self.root, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=7, column=0, columnspan=2)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=8, column=0, columnspan=2)

        self.contacts_listbox = tk.Listbox(self.root, width=50)
        self.contacts_listbox.grid(row=9, column=0, columnspan=2)

    def add_contact(self):
        contact = {
            "name": self.name_var.get(),
            "phone": self.phone_var.get(),
            "email": self.email_var.get(),
            "address": self.address_var.get()
        }
        self.contacts.append(contact)
        messagebox.showinfo("Success", f"Contact {contact['name']} added successfully.")
        self.clear_fields()

    def view_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def search_contact(self):
        keyword = self.name_var.get()
        self.contacts_listbox.delete(0, tk.END)
        results = [contact for contact in self.contacts if keyword.lower() in contact['name'].lower() or keyword in contact['phone']]
        if not results:
            self.contacts_listbox.insert(tk.END, "No contacts found.")
        else:
            for contact in results:
                self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def update_contact(self):
        name = simpledialog.askstring("Update Contact", "Enter the name of the contact to update:")
        if not name:
            return
        
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                new_phone = simpledialog.askstring("Update Contact", "Enter new phone number (leave blank to skip):")
                new_email = simpledialog.askstring("Update Contact", "Enter new email (leave blank to skip):")
                new_address = simpledialog.askstring("Update Contact", "Enter new address (leave blank to skip):")
                
                if new_phone:
                    contact['phone'] = new_phone
                if new_email:
                    contact['email'] = new_email
                if new_address:
                    contact['address'] = new_address
                
                messagebox.showinfo("Success", f"Contact {name} updated successfully.")
                self.clear_fields()
                return
        messagebox.showerror("Error", f"Contact {name} not found.")

    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter the name of the contact to delete:")
        if not name:
            return
        
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                self.contacts.remove(contact)
                messagebox.showinfo("Success", f"Contact {name} deleted successfully.")
                self.clear_fields()
                return
        messagebox.showerror("Error", f"Contact {name} not found.")

    def clear_fields(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()