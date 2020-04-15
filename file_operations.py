import shutil
import os

def del_folder(path):
    shutil.rmtree(path)
    print(path+" deleted.")

def create_folder(path):
    os.mkdir(path)
    print(path+" created.")

def del_file(filepath):
    os.remove(filepath)
    print(filepath+" deleted.")

