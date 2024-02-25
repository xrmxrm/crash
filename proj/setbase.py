import os

def set_base(basedir):
    """Set base directory and make it the current working directory"""
    os.chdir(basedir)
    return basedir
