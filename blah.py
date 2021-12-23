import os

list = []

for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
        a = os.path.join(root, name)
        b = a.replace(".", "", 1)
        c = b.replace("\\", "/")
        list.append(c)
   for name in dirs:
        a = os.path.join(root, name)
        b = a.replace(".", "", 1)
        c = b.replace("\\", "/")
        list.append(c)

print(list)

