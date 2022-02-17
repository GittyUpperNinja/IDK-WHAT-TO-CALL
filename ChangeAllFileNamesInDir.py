import os

Name = "Hand_Motion"

path = os.path.dirname(os.path.realpath(__file__))

i =0
for file in os.listdir(path):
    if (".jpg" in file):
        newFileName = Name + "[" + str(i) + "]"
        os.rename(path + "/" + file, newFileName + ".jpg")
        i += 1
