import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    print(os.name)
    
    
print("Item exists:", str(path.exists("textfile.txt")))
print("Item is a file:", path.isfile("textfile.txt"))
print("Item is a directory:",path.isdir("textfile.txt"))


print("Item's path:", path.realpath("textfile.txt"))
print("Item's path and name:", path.split(path.realpath("textfile.txt")))

t = time.ctime(path.getmtime("textfile.txt"))
print(t)
print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))