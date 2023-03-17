#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
#     # Print the name of the OS
#     print(os.name)
#
#     # Check for item existence and type
# print("Item exists: ", str(path.exists("textfile.txt"))) # textfile.txt'nin varligi sorgulaniyor.
# print("Item is a file: ",path.isfile("textfile.txt"))   # textfile.txt'nin dosya olup olmadigi sorgulaniyor.
# print("Item is a directory: ", path.isdir("textfile.txt")) # textfile.txt'nin klasor olup olmadigi sorgulaniyor.
#
#     # Work with file paths
# print("Item's path:", path.realpath("textfile.txt")) # dosyanin yolu yazdiriliyor
# print("Item's path:", path.split(path.realpath("textfile.txt"))) # dosya yolu ve adi ayri ayri yazdiriliyor
#
    # Get the modification time
    t= time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
    
    # Calculate how long ago the item was modified
    td=datetime.datetime.now()- datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been", td, "since the file was modified")
    print("Or,", td.total_seconds(), "seconds")
  
if __name__ == "__main__":
    main()
