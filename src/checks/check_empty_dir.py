import os
from src.docs import needed_files, needed_folders

def check_empty_dir(path: str) -> bool:
    file_list = set(os.listdir(path))

    return len(needed_files & file_list) == 0 and len(needed_folders & file_list) == 0