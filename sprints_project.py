import re
import os
from datetime import date
import csv
from os import path


def Contact_Book():
    options = input(
        "Hello, please choose:\n1: Create Records \t2: update \t3: delete\t4: quit\n")
    if options == '1':
        records()
    elif options == '2':
        update()
    elif options == '3':
        delete()
    elif options == '4':
        print("Goodbye")
        return 1
    else:
        print("please enter one of these options ")

    Contact_Book()


def records():
    # name
    name = input("Please Enter Your Name:  \n")
    while not re.fullmatch("[A-Za-z]+[ [A-Za-z]+]*", name):
        print("Make sure you only use letters in your name ")
        name = input("Please enter your name again: \n")
    # valid email
    email = input("Please enter your email : \n")
    while not re.match(r"\b[A-Za-z0-9._%+-]+\@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", email):
        print("Invalid email, Make sure your Email in right format ")
        email = input("Please enter your Email again: \n")
    # valid phone numbers
    phone = input("please enter your phone number:  \n")
    while not re.match(r"(\+02)* *01+[1,0,2,5][0-9]{8}$", phone):
        print("Invalid phone number,Make sure your phone number is in right format ")
        phone = input("please enter your phone number again: \n")
        #
        # another_phone = input("Enter another number?? ( y / n )")
        # if another_phone == 'n':
        #          pass

    # return input(phone)
    # home address
    address = input("Please enter your home address: \n ")
    # date
    today = (date.today()).strftime("%d/%m/%Y")
    data = [name, email, address, phone, today]

    filename = str("contactbook_" + str((date.today()).strftime("%d-%m-%Y")) + ".csv")
    with open(filename, 'a+', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, address, phone, today])


def update():
    fname = input("plz enter file name: ")
    if not path.exists(fname):
        print("the file is not exist, try again")
        return "Null"
    name=input("which contact you want to update his info: ")
    record = input("which record you want to change (name , email , phone , address):")
    new_record = input("plz Enter your new record: ")
    filename = str("contactbook_" + str((date.today()).strftime("%d-%m-%Y")) + ".csv")
    file = open(filename, 'r')
    reader = csv.reader(file)  # Read the file will be updated
    rows = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                if record == "name":
                    row[0] = new_record
                elif record == "email":
                    row[1] = new_record
                elif record == "address":
                    row[2] = new_record
                elif record == "phone":
                    row[3] = new_record
            rows.append(row)
    with open(filename, 'w', newline='') as update:
        write = csv.writer(update)
        write.writerows(rows)


def delete():
    rows =[]
    name = input("Enter the user name: ")
    filename = str("contactbook_" + str((date.today()).strftime("%d-%m-%Y")) + ".csv")
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            if line[0] == name:
                continue
            else:
                rows.append(line)
    with open(filename, 'w', newline='') as update:
        csv_writer = csv.writer(update)
        csv_writer.writerows(rows)







Contact_Book()
