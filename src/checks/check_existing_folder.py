import os

def check_existing_folder(path: str):
    folder_exists: bool = os.path.isdir(path)

    if not folder_exists:
        # create folder
        os.makedirs(path)
