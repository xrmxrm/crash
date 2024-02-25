import os
import json
from pathlib import Path


def set_base(basedir):
    """Set base directory and make it the current working directory"""
    os.chdir(basedir)
    return basedir

base = set_base('/home/richard/Dev/Py/crash/proj/guest')

path = Path(f'{base}/username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")