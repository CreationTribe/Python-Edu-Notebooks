import os

dirname = input("Enter the directory: ")
os.chdir(dirname)
dirlist = os.listdir

picture_number = 1

for filename in dirlist:
    if filename.endswith('.jpg'):
        newname = "sumvac"+str(picture_number)+".jpg"
        os.rename(filename, newname)
        picture_number += 1

