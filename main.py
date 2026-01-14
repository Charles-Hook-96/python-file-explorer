import os
from frame import build_explorer

def open_window():
    build_explorer()

def get_file_path():
    return os.path.curdir

if __name__ == '__main__':
    open_window()
