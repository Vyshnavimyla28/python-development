import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
    else:
        # Here you can add code to save the data, for example, to a database or a file
        messagebox.showinfo("Success", "Registration Successful")

# Create the main application window
root = tk.Tk()
root.title("Registration Form")
root.geometry("300x300")

# Create labels and entry widgets for the form fields
name_label = tk.Label(root, text="Name")
name_label.pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

email_label = tk.Label(root, text="Email")
email_label.pack(pady=5)
email_entry = tk.Entry(root)
email_entry.pack(pady=5)

password_label = tk.Label(root, text="Password")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

confirm_password_label = tk.Label(root, text="Confirm Password")
confirm_password_label.pack(pady=5)
confirm_password_entry = tk.Entry(root, show="*")
confirm_password_entry.pack(pady=5)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
