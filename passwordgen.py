 #!/usr/bin/env python3
import random, getpass, os
from Crypto.Cipher import DES

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
        myFile.write(domain + ': '+ my_pass + "\n")

def check_domain(domain):
    if domain in read_file(passwordFilePath):
        print("This ",  domain ," already exists")
        quit()
    else:
        create_mypass(my_pass)

des = DES.new('01234567', DES.MODE_ECB)
alphabet= ("0123456789abcdefghjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/")
pass_length = 8
my_pass = ("")
password1 = ("abcd")
word_list = []
passwordFilePath = "/home/callum/Documents/PasswordGen/password.txt"

domain = raw_input("Enter the domain this password is for: ")

check_domain(domain)


