import shutil, os
from pathlib import Path

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
            if not file_name.endswith(".py"):
                try:
                    shutil.copy(source, destination)

                except shutil.SameFileError:
                    print("File already exists in source and destination.")

                except PermissionError:
                    print("Permission Denied.")

                except:
                    print("Error occurred while copying file.")

main()