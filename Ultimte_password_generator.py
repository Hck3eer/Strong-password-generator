import tkinter as tk
from tkinter import messagebox, filedialog
import string
import random
import pyperclip

def generate_password():
    try:
        length = int(length_var.get())
        if length < 4:
            messagebox.showwarning("Too Short", "Password length must be at least 4.")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a valid number for length.")
        return

    charset = ""
    if use_upper.get():
        charset += string.ascii_uppercase
    if use_lower.get():
        charset += string.ascii_lowercase
    if use_digits.get():
        charset += string.digits
    if use_symbols.get():
        charset += string.punctuation
    if not charset:
        messagebox.showwarning("Empty Selection", "Select at least one character type.")
        return

    if avoid_similar.get():
        for c in "Il1O0":
            charset = charset.replace(c, "")

    password = ''.join(random.choice(charset) for _ in range(length))
    entry_result.delete(0, tk.END)
    entry_result.insert(0, password)

def copy_password():
    password = entry_result.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

def save_password():
    password = entry_result.get()
    if not password:
        messagebox.showwarning("No Password", "Generate a password first.")
        return
    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if path:
        with open(path, "w") as f:
            f.write(password)
        messagebox.showinfo("Saved", f"Password saved to {path}")

def clear_fields():
    entry_result.delete(0, tk.END)
    length_var.set("12")
    use_upper.set(True)
    use_lower.set(True)
    use_digits.set(True)
    use_symbols.set(True)
    avoid_similar.set(False)

# GUI Setup
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("500x450")
root.resizable(False, False)

tk.Label(root, text="Password Length:").pack(pady=5)
length_var = tk.StringVar(value="12")
tk.Entry(root, textvariable=length_var, width=5, justify='center').pack()

# Checkboxes for character types
use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)
avoid_similar = tk.BooleanVar(value=False)

frame_checks = tk.Frame(root)
frame_checks.pack(pady=5)

tk.Checkbutton(frame_checks, text="Uppercase (A-Z)", variable=use_upper).grid(row=0, column=0, sticky="w", padx=10)
tk.Checkbutton(frame_checks, text="Lowercase (a-z)", variable=use_lower).grid(row=1, column=0, sticky="w", padx=10)
tk.Checkbutton(frame_checks, text="Digits (0-9)", variable=use_digits).grid(row=2, column=0, sticky="w", padx=10)
tk.Checkbutton(frame_checks, text="Symbols (!@#$)", variable=use_symbols).grid(row=3, column=0, sticky="w", padx=10)
tk.Checkbutton(frame_checks, text="Avoid Similar (Il1O0)", variable=avoid_similar).grid(row=4, column=0, sticky="w", padx=10)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

entry_result = tk.Entry(root, width=40, font=('Courier', 12), justify='center')
entry_result.pack(pady=5)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Copy", command=copy_password).grid(row=0, column=0, padx=10)
tk.Button(frame_buttons, text="Save to File", command=save_password).grid(row=0, column=1, padx=10)
tk.Button(frame_buttons, text="Clear", command=clear_fields).grid(row=0, column=2, padx=10)

root.mainloop()
