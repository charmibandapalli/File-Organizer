import os, shutil

files = os.listdir()
for file in files:
    if file.endswith(".jpg"):
        shutil.move(file, "Images/")
    elif file.endswith(".txt"):
        shutil.move(file, "Documents/")
