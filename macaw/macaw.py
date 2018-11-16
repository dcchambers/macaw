#!/usr/bin/env python3

# Macaw
#
# Testing file open and string concatenation.

import random

def main():
    password = ''

    # This dictionary of words is for testing only and should *not* be considered secure.
    # Courtesy of https://gist.github.com/deekayen/4148741
    f = open('dictionary.txt')
    wordList = f.read().split()

    for i in range(0, 5):
        word = wordList[random.randint(0,999)] # grab a random word from the dictionary file.
        password = password + word #concat that word to the end of the password.
        
    print(password)
    #print("Macaw!") #DEBUG

main()
