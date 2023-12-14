#import tkinter as tk
#from tkinter import messagebox
import sqlite3

# Function to fetch user details from the database
def fetch_user_details():
    user_id = int(id_entry.get())
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
    user_details = cursor.fetchone()
    conn.close()

    # Display user details if found
    if user_details:
        id_label.config(text="ID: " + str(user_details[0]))
        name_label.config(text="Name: " + user_details[1])
        email_label.config(text="Email: " + user_details[2])
    else:
        id_label.config(text="User not found")
        name_label.config(text="")
        email_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Fetch User Details")

# Create input label and entry field for ID
id_label = tk.Label(root, text="Enter User ID:")
id_label.pack()
id_entry = tk.Entry(root)
id_entry.pack()

# Create button to fetch details
fetch_button = tk.Button(root, text="Fetch Details", command=fetch_user_details)
fetch_button.pack()

# Labels to display user details
id_label = tk.Label(root, text="")
id_label.pack()
name_label = tk.Label(root, text="")
name_label.pack()
email_label = tk.Label(root, text="")
email_label.pack()

# Run the application
root.mainloop()