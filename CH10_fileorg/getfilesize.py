import shutil, os
from pathlib import Path
import send2trash

def main():
    print()
    path = '/workspaces/115507760/'
    destination = os.path.join(os.path.abspath('.'), 'copyofallnonpyfiles')
    for folder_name, sub_folders, file_names in os.walk(path):
        sub_folders[:] = [sub_folder
                       for sub_folder in sub_folders
                       if sub_folder[0] != '.']
        for file_name in file_names:
            source = os.path.join(folder_name, file_name)
            file_info = os.path.getsize(source)
            if file_info > 100000:
                send2trash.send2trash(source)
                print(file_name)

main()