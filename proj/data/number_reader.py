import os
import json
from pathlib import Path

def set_base(basedir):
    """Set base directory and make it the current working directory"""
    os.chdir(basedir)
    return basedir

base = set_base('/home/richard/Dev/Py/crash/proj/data')

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)