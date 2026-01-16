import tkinter as tk
from tkinter import TclError, ttk, filedialog
from explorer_content import *

def build_root_window() -> tk.Tk:
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

def build_inner_frame(root) -> tk.Frame:
    inner_frame = ttk.Frame(root, padding="15", relief="sunken")
    inner_frame.pack(fill='both', expand=True, padx=15, pady=15)
    return inner_frame

def build_explorer_frame(inner_frame):
    paned = ttk.Panedwindow(inner_frame, orient='horizontal')
    paned.pack(fill='both', expand=True)

    left_frame = ttk.Frame(paned, relief='sunken', borderwidth=1)
    paned.add(left_frame, weight=1)

    right_frame = ttk.Frame(paned, relief='sunken', borderwidth=1)
    paned.add(right_frame, weight=3)

    tree = ttk.Treeview(left_frame)
    tree.pack(fill='both', expand=True)

    tree.insert('', 'end', text=str(get_file_path()))
    tree.insert('', 'end', text='Folder 2')



def build_explorer():
    root = build_root_window()
    inner_frame = build_inner_frame(root)
    build_explorer_frame(inner_frame)
    root.mainloop()