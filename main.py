import tkinter as tk
from tkinter import TclError, ttk

def open_window():
    root = build_root_window()

    message = tk.Label(root, text="Hello World")
    message.pack()

    root.mainloop()

def build_root_window():
    root = tk.Tk()

    window_width = int(root.winfo_screenwidth() / 2)
    window_height = int(root.winfo_screenheight() / 1.75)

    center_x = int(root.winfo_screenwidth() / 2 - window_width / 2)
    center_y = int(root.winfo_screenheight() / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.title("Python File Explorer")
    root.iconbitmap("./assets/python-folder-icon.ico")

    return root

def get_file_path():
    pass

if __name__ == '__main__':
    open_window()
