import os
import shutil
source = input("Please Enter Source Folder Name ")
destination = input("Please Enter Destination Folder Name ")
source = source + "/"
destination = destination + "/"
listOfFiles = os.listdir(source)
print(listOfFiles)
for file in listOfFiles:
    shutil.move((source+file),(destination))
    