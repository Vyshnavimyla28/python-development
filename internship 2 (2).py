import tkinter as tk
from tkinter import scrolledtext

# Function to handle sending messages
def send_message():
    message = entry_box.get()
    if message:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + message + '\n')
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)
        entry_box.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Chatbox")
root.geometry("400x500")

# Create a scrolled text widget for the chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD)
chat_window.config(state=tk.DISABLED)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create an entry widget for the user to type messages
entry_box = tk.Entry(root, width=80)
entry_box.pack(padx=10, pady=(0, 10), fill=tk.X)

# Create a send button to send the message
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
