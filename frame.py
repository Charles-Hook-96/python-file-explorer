import tkinter as tk
from tkinter import TclError, ttk, filedialog

def build_root_window():
    root = tk.Tk()
    root.configure(background="grey")

    window_width = int(root.winfo_screenwidth() / 2)
    window_height = int(root.winfo_screenheight() / 1.75)

    center_x = int(root.winfo_screenwidth() / 2 - window_width / 2)
    center_y = int(root.winfo_screenheight() / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.title("Python File Explorer")
    root.iconbitmap("./assets/python-folder-icon.ico")

    return root

def build_inner_frame(root):
    inner_frame = ttk.Frame(root, padding="15", relief="sunken")
    inner_frame.pack(fill='both', expand=True, padx=15, pady=15)

def build_explorer():
    root = build_root_window()
    build_inner_frame(root)
    root.mainloop()