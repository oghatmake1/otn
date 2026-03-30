import shutil as stil
import os
import json

old = r"C:\Users\PC\Downloads\py test env\sfxold"
new = r"C:\Users\PC\Downloads\py test env\sfxnew"

with open("oldtonew.json", "rt") as f:
    replacements = json.load(f)

def move(a: str, b: str):
    os.makedirs(os.path.dirname(b), exist_ok=True)
    stil.move(a, b)

def list_files(path):
    file_list = []
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            rel_dir = os.path.relpath(dirpath, path)
            if rel_dir == '.':
                file_list.append(f)
            else:
                file_list.append(os.path.join(rel_dir, f).replace("/", "\\"))
    return file_list

for i in list_files(old):
    try:
        src = os.path.join(old, i)
        dst = os.path.join(new, replacements[i])
        print(src, "->", dst)
        move(src, dst)
    except Exception as e:
        print(f"Error with {i}: {e}")
