import os

DATA_DIR='supporting'
_ROOT = os.path.abspath(os.path.dirname(__file__))

def get_data(path):
    return os.path.join(_ROOT, DATA_DIR, path)
