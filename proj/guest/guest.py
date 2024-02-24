import os
from pathlib import Path

def set_base(basedir):
    """Set base directory and make it the current working directory"""
    os.chdir(basedir)
    return basedir

base = set_base('/home/richard/Dev/Py/crash/proj')

guest_name = input('Name: ')
file_name = guest_name.strip()+'.txt'
path=Path(f'{base}/guest/{file_name}')

print(f"Writing '{guest_name}' to '{file_name}' using path "
      f"'{path}' from '{os.getcwd()}'")
      
path.write_text(guest_name)

