 #!/usr/bin/env python3
import random, getpass, os
from Crypto.Cipher import DES


des = DES.new('01234567', DES.MODE_ECB)
alphabet= ("0123456789abcdefghjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/")
pass_length = 8
password1 = ("abcd")
word_list = []
my_pass = ("")
master_pass = ("")
passwordFilePath = ("/home/callum/Documents/PasswordGen/password.txt")
domain = ("")
masterPassFile = ("/home/callum/Documents/PasswordGen/masterPasword.txt")

def master_parseLine(line):
    master, password = line.split(":", 1)
    master = master.strip()
    password = password.strip()
    return master, password

def read_masterFile(path):
    entries = {}
    for line in open(path):
        master, password = master_parseLine(line)
        entries[master] = password
    return entries

def Create_MasterPass(master):
    master_pass = getpass.getpass("Please enter what you would like to be your master password: ")
    master_passCheck = getpass.getpass("Please re-enter master password: ")
    if master_pass  != master_passCheck:
        print("The passwords you entered did not match")
        quit()
    elif master_pass ==  master_passCheck:
        print("Password accepted")
        with open(masterPassFile, 'a') as masterFile:
            masterFile.write("Master password: " + master_pass +"\n")
Create_MasterPass(master_pass)

domain = raw_input("Enter the domain this password is for: ")

def parse_line(line):
    domain, password = line.split(":", 1)
    domain = domain.strip()
    password = password.strip()
    return domain, password


def read_file(path):
    entries = {}
    for line in open(path):
        domain, password = parse_line(line)
        entries[domain] = password
    return entries

def create_mypass(password):
    my_pass = ("")
    for i in range(pass_length):
        next_index = random.randrange(len(alphabet))
        my_pass = my_pass + alphabet[next_index]
    with open(passwordFilePath, "a") as myFile:
        myFile.write((domain) + ': '+ my_pass + "\n")

def check_domain(domain):
    if domain in read_file(passwordFilePath):
        print("The domain: " + domain + " already exists")
    else:
        create_mypass(my_pass)


check_domain(domain)
