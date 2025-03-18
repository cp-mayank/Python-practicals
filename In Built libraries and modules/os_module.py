
# -> Create a program that lists all files and directories in the current directory.

import os

def list_files_and_directories():
    items = os.listdir('.')
    for item in items:
        print(item)

list_files_and_directories()
