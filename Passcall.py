#!/usr/bin/env python
import getpass
from Crypto.Cipher import DES

des = DES.new('01234567', DES.MODE_ECB)
alphabet = ("abcdefgh12345678")
pass1 = ('abcd')
cipher_text = des.encrypt(alphabet)

if getpass.getpass('Enter Password: ') != pass1:
    print (cipher_text)
else:
    f = open("password.txt","r")
    print(f.read())
    f.close()
