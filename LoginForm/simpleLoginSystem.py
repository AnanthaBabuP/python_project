import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Screen")

# Create username label and entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, sticky="w")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

# Create password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, sticky="w")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

# Create login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
