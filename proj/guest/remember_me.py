import os
import json
from pathlib import Path

def set_base(basedir):
    """Set base directory and make it the current working directory"""
    os.chdir(basedir)
    return basedir

base = set_base('/home/richard/Dev/Py/crash/proj/guest')

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Greet user by name"""
    path = Path(f'{base}/username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()