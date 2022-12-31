import shutil, os
from pathlib import Path

def main():
    path = '/workspaces/115507760/ATBS/CH10_fileorg/spamfiles/'
    for folder_name, sub_folders, file_names in os.walk(path):
        sub_folders[:] = [sub_folder for sub_folder in sub_folders if sub_folder[0] != '.']
        # for file_name in file_names:
        #     print(file_name)
        file_names.sort()
        for file_name in file_names:
            if file_name.startswith('spam') and file_name.endswith('.txt'):

main()