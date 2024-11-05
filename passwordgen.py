import random
import pyperclip
import customtkinter as ctk
from tkinter import messagebox

# Initialize customtkinter theme
ctk.set_appearance_mode("System")  # Use system theme (light or dark)
ctk.set_default_color_theme("blue")  # Default theme

# Function to generate a password
def generate_password():
    text = '1234567890QWERTYUIOP[]\\ASDFGHJKLZXCVBNM./qwertyuiopasdfghjklzxcvbnm;:<>?{}#%!()_-=+'
    alphabet = list(text)
    password = ''.join(random.sample(alphabet, k=20))
    password_var.set(password)

# Function to copy password to clipboard
def copy_password():
    pyperclip.copy(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Setting up the modern GUI

# App title
root = ctk.CTk()
root.title("Password Generator")
root.geometry("400x250")

password_var = ctk.StringVar()

# Password display and buttons
ctk.CTkLabel(root, text="Generated Password:", font=("Arial", 16)).pack(pady=10)
password_entry = ctk.CTkEntry(root, textvariable=password_var, font=("Arial", 14), width=280)
password_entry.pack(pady=5)

generate_button = ctk.CTkButton(root, text="Generate Password", command=generate_password, width=200, height=40)
generate_button.pack(pady=10)

copy_button = ctk.CTkButton(root, text="Copy Password", command=copy_password, width=200, height=40)
copy_button.pack(pady=5)

# Start the GUI loop
root.mainloop()