import os
from pathlib import Path

def set_base(basedir):
    """Set base directory and make it the current working directory"""
    os.chdir(basedir)
    return basedir

base = set_base('/home/richard/Dev/Py/crash/proj/guest')

def get_names():
    contents = ''
    while (True):
        name = input("Name: ")
        if name:
            contents += name.strip().title() + '\n'
        else:
            break
    return contents

path = Path(f'{base}/guest_book.txt')
path.write_text(get_names())