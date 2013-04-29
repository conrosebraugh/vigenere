#!/usr/bin/python2.7

import sys
import itertools

def getMsg():
    return raw_input("Enter the message: ").upper().replace(" ","")

def getKey():
    return raw_input("Enter the key: ").split()

def getMode():
    while True:
        mode = raw_input('Would you like to encrypt or decrypt a message? ').lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt"/"e" or "decrypt"/"d"')
            print()

# def getKey():
#     key = ''
#     while not key.isalpha():
#         key = raw_input('Please enter the key: ')
#         if not key.isalpha():
#             print('Key must be a word without numbers or spaces')
#             print
#     return key.upper()

def getKeyLen():
    keyLen = raw_input('Key Length: ')
    return int(keyLen)

def getWordLen():
    keyLen = raw_input('Word Length: ')
    return int(keyLen)

def genKeyList(keyLen):
    x = itertools.permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZ', keyLen)
    lot = []
    for i in x:
        lot.append(i)

    keyList = []
    for j in lot:
        keyList.append(''.join(list(i)))

    return keyList

def fitKey(msg, k):
    msg = ''.join(msg.split())
    while len(msg) > len(k):
        k += k
    return k

def encrypt(msg, k):
    emsg = ''

    i = 0
    for l in msg:
        emsg += chr((((ord(l)-65) + (ord(k[i])-65))%26)+65)
        i += 1
        
    return emsg

def decrypt(msg, k):
    dmsg = ''
    
    i = 0
    for l in msg:
        dmsg += chr((((ord(l)-65) - (ord(k[i])-65))%26)+65)
        i += 1
        
    return dmsg

f = open('dict.txt', 'r')
thedict = [[] for i in range(18)]
for line in f:
    # print line
    thedict[len(line)-2].append(line[:len(line)-2])



print
print("Welcome to Connar's Vigenere Cypher Program")
print
print

choice = "yes"

while choice == 'y' or choice == 'Y' or choice == 'yes':
    #mode = getMode()
    message = getMsg()
    keyLen = getKeyLen()
    wordLen = getWordLen()
    keyPossibilities = thedict[wordLen]

    keyList = genKeyList(keyLen)

    print keyPossibilities

    #key = getKey()
    # key = fitKey(message, key)
    # if mode.startswith('e'):
    #     print encrypt(message, key)
    # else:
    #     print decrypt(message, key) 

    # print 

    # choice = raw_input("Again? ")


print "Goodbye"
