#os mod provides functions to interact with OS
import os

#walk() generates the file names in a directory tree by walking the tree either top-down or bottom-up
for path, dirs, files in os.walk("C:/Users/Shashvath/Pictures"):
    print("he current folder is : " + path)
    for dir in dirs:
        print("Subfolder is : " + path + dir)
    for file in files:
        print("Folder : " + path + file)