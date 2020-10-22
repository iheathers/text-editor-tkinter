import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Field and Labels')


def greet():
    print(f"Hello, {username.get()}")


button = ttk.Button(root, text="Greet", command=greet)
button.pack(side='left', fill='x', expand=True)

username = tk.StringVar()

name_label = ttk.Label(root, text="Name: ")
name_label.pack(side='left', padx=(10, 10))

name_entry = ttk.Entry(root, width=20, textvariable=username)
name_entry.pack(side='left')
name_entry.focus()

root.mainloop()
