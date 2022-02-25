import os
#from os import path
from csv import writer


def data_entry():
    print("Welcome to Steve Colletta's file application.")
    print("")
    fileplace = input("Please enter a folder for a place to save a file, e.g. 'c:/test/': ")
    while (True):
        if not os.path.exists(fileplace):
            answer = input("That folder does not exist. Type 'yes' or 'y' if you wish to create that folder: ")
            if answer == "yes" or answer == "y":
                while True:
                    os.mkdir(fileplace)
                    print (fileplace, "created")
                    break
            else:
                print("Ok, try again.")
                fileplace = input("Please enter a folder for a place to save a file. 'c:/test/': ")
        else:
            break
    filename = input("Please type in the name of a file that we will create for data entry: ")
    ffn = os.path.join(fileplace, filename)
    with open(ffn, 'w') as file1:
        name = input("type in a name: ")
        address = input("type in an address: ")
        phone = input("type in a phone number: ")
        info = [name, address, phone]
        writer_object = writer(file1)
        writer_object.writerow(info)
        file1.close()
    with open(ffn, 'r') as file2:
        lines = file2.read()
        print(lines)
        file2.close()


data_entry()
