import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title("Greeting")


def greet():
    print("Hello, Tkinter")


button = ttk.Button(root, text="Greet", command=greet)
button.pack(side='left', fill='x', expand=True)


quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side='left', fill='x', expand=True)

root.mainloop()
