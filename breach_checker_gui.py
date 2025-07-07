import tkinter as tk
from tkinter import messagebox

def load_emails(filename):
    emails = set()
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            email = line.strip().lower()
            if "@" in email:
                emails.add(email)
    return emails

def load_passwords(filename):
    passwords = set()
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            pwd = line.strip()
            if pwd:
                passwords.add(pwd)
    return passwords

# Load breach data
print("Loading breach data, please wait...")
emails_set = set()
passwords_set = set()
emails_set.update(load_emails('/home/senuri/Downloads/linkedin_data.csv'))
emails_set.update(load_emails('/home/senuri/seclists_valid_emails.txt'))
passwords_set.update(load_passwords('/usr/share/seclists/Passwords/Common-Credentials/500-worst-passwords.txt'))
print(f"Loaded {len(emails_set)} unique emails and {len(passwords_set)} passwords.")

def check_email():
    email = email_entry.get().strip().lower()
    if email in emails_set:
        messagebox.showwarning("Breach Result", f"⚠️ {email} was FOUND in breach data!")
    else:
        messagebox.showinfo("Breach Result", f"✅ {email} was NOT found in breach data.")

def check_password():
    pwd = password_entry.get().strip()
    if pwd in passwords_set:
        messagebox.showwarning("Breach Result", "⚠️ This password was FOUND in breach data!")
    else:
        messagebox.showinfo("Breach Result", "✅ This password was NOT found in breach data.")

# GUI
root = tk.Tk()
root.title("Breach Notifier")

# Set overall window style
root.configure(bg="#2c3e50")  # dark blue-gray background

# Common font for widgets
FONT = ("Helvetica", 12)

# Title label
title_label = tk.Label(
    root,
    text="🔎 Breach Notifier",
    font=("Helvetica", 20, "bold"),
    bg="#2c3e50",
    fg="#ecf0f1",  # light text
)
title_label.grid(row=0, column=0, columnspan=3, pady=(20, 20))

# Email checker
tk.Label(root, text="Enter email to check:", font=FONT, bg="#2c3e50", fg="#ecf0f1").grid(
    row=1, column=0, sticky='w', padx=10, pady=10
)
email_entry = tk.Entry(root, width=50, font=FONT)
email_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(
    root,
    text="Check Email",
    command=check_email,
    bg="#3498db",      # blue button
    fg="white",
    font=FONT,
    activebackground="#2980b9",
).grid(row=1, column=2, padx=10, pady=10)

# Password checker
tk.Label(root, text="Enter password to check:", font=FONT, bg="#2c3e50", fg="#ecf0f1").grid(
    row=2, column=0, sticky='w', padx=10, pady=10
)
password_entry = tk.Entry(root, show='*', width=50, font=FONT)
password_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Button(
    root,
    text="Check Password",
    command=check_password,
    bg="#e67e22",       # orange button
    fg="white",
    font=FONT,
    activebackground="#d35400",
).grid(row=2, column=2, padx=10, pady=10)

# Exit button
tk.Button(
    root,
    text="Quit",
    command=root.quit,
    bg="#c0392b",       # red button
    fg="white",
    font=FONT,
    activebackground="#922b21",
    width=20,
).grid(row=3, column=0, columnspan=3, pady=(20, 20))

root.mainloop()
