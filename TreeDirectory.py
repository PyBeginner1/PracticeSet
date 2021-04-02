import os

for path, dirs, files in os.walk("C:/Users/Shashvath/Pictures"):
    print("he current folder is : " + path)
    for dir in dirs:
        print("Subfolder is : " + path + dir)
    for file in files:
        print("Folder : " + path + file)