from distutils import extension
import os
import shutil
path = input("Enter the Path of the Folder ")
path = path + "/"
listOfFiles = os.listdir(path)
print(listOfFiles)
for file in listOfFiles:
    name,ext = os.path.splitext(file)
    ext = ext[1:]
    if(ext == ''):
        continue
    if os.path.exists(path + "/" + ext):
        shutil.move(path + "/" + file, path + "/" + ext + "/" + file)
    else: 
        os.makedirs(path + "/" + ext)
        shutil.move(path + "/" + file, path + "/" + ext + "/" + file)