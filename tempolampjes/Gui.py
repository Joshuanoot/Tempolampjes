import tkinter as tk
from tkinter import filedialog
import subprocess  # Add this line to import the subprocess module
import signal
# Initialize process variable
process = None

# Save the original content of testedit.py when the program starts
original_content = ""

def on_run_button_click():
    global process
    if process and process.poll() is None:
        # Terminate the existing subprocess if it's still running
        process.terminate()
        process.wait()  # Wait for the process to finish

    file_path = filedialog.askopenfilename(title="Select a Python file", filetypes=[("Python files", "*.py")])
    if file_path:
        process = subprocess.Popen(["python", file_path, "12"])

def on_stop_button_click():
    global process
    if process and process.poll() is None:
        # Send a KeyboardInterrupt signal to the subprocess
        process.send_signal(signal.SIGINT)
        process.wait()  # Wait for the process to finish

def on_open_button_click():
    file_path = filedialog.askopenfilename(title="Select a Python file", filetypes=[("Python files", "*.py")])
    if file_path:
        # Add your code for opening a Python file in Thonny here
        pass

def on_edit_button_click():
    file_path = "testedit.py"  # Specific file to edit
    old_word = "50"  # Replace with the word you want to replace
    new_word = entry.get()

    try:
        # Read the entire content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Replace the old word with the new word
        updated_content = content.replace(old_word, new_word)

        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.write(updated_content)

    except Exception as e:
        error_message = f"Error editing the file: {str(e)}"
        print(error_message)  # You can also show this message in a messagebox or other GUI element

def on_reset_button_click():
    file_path = "testedit.py"  # Specific file to reset
    try:
        # Write the original content back to the file
        with open(file_path, 'w') as file:
            file.write(original_content)

    except Exception as e:
        error_message = f"Error resetting the file: {str(e)}"
        print(error_message)  # You can also show this message in a messagebox or other GUI element

# Read the original content of testedit.py when the program starts
with open("testedit.py", 'r') as file:
    original_content = file.read()

# Create the main window
root = tk.Tk()
root.title("Tempolampjes")

# Set the window geometry to 800x600 pixels
root.geometry("500x500")

# ... (rest of your script)


# Create and pack widgets with larger buttons
run_button = tk.Button(root, text="Run", command=on_run_button_click, width=20, height=3)
run_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=on_stop_button_click, width=20, height=3)
stop_button.pack(pady=10)

open_button = tk.Button(root, text="Edit file", command=on_open_button_click, width=20, height=3)
open_button.pack(pady=10)

# Entry for user input
entry_label = tk.Label(root, text="Enter new speed:")
entry_label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Button to replace specific word in testedit.py
edit_button = tk.Button(root, text="New speed", command=on_edit_button_click, width=20, height=3)
edit_button.pack(pady=10)

# Button to reset the content of testedit.py to a default word
reset_button = tk.Button(root, text="Reset to old speed", command=on_reset_button_click, width=20, height=3)
reset_button.pack(pady=10)

# Start the main loop
root.mainloop()
