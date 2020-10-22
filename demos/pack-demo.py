import tkinter as tk

root = tk.Tk()

tk.Label(root, text='Label 1', bg='green').pack(side='left', fill='y', expand=True)
tk.Label(root, text='Label 2', bg='red').pack(side='top', fill='x', expand=True)
tk.Label(root, text='Label 3', bg='yellow').pack(side='left', fill='both ', expand=True)

root.mainloop()
