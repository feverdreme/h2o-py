import os
from src.docs import needed_files

def check_initted_dir():
    if len(needed_files & set(os.listdir())) == len(needed_files):
        pass

    else:
        raise "Install error: directory must be initialized"
