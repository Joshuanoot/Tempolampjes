import tkinter as tk
from tkinter import filedialog
import os

def on_run_button_click():
    # Add your code for running a Python file here
    pass

def on_stop_button_click():
    # Add your code for stopping execution here
    pass

def on_open_button_click():
    file_path = filedialog.askopenfilename(title="Select a Python file", filetypes=[("Python files", "*.py")])
    if file_path:
        # Add your code for opening a Python file in Thonny here
        pass

def on_edit_button_click():
    file_path = "testedit.py"  # Specific file to edit
    new_content = entry.get()
    
    with open(file_path, 'a') as file:
        file.write('\n' + new_content)

# Create the main window
root = tk.Tk()
root.title("Python File Editor")

# Set the window geometry to 500x450 pixels
root.geometry("500x450")

# Create and pack widgets with larger buttons
run_button = tk.Button(root, text="Start", command=on_run_button_click, width=20, height=3)
run_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=on_stop_button_click, width=20, height=3)
stop_button.pack(pady=10)

open_button = tk.Button(root, text="Edit in python", command=on_open_button_click, width=20, height=3)
open_button.pack(pady=10)

# Entry for user input
entry_label = tk.Label(root, text="Enter text for file:")
entry_label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Button to edit specific Python file
edit_button = tk.Button(root, text="Edit", command=on_edit_button_click, width=20, height=3)
edit_button.pack(pady=10)

# Start the main loop
root.mainloop()

