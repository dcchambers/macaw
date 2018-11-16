#!/usr/bin/env python3

# Macaw
#
# Testing file open and string concatenation.

def main():
    password = ''
    # This dictionary of words is for testing only and should *not* be considered secure.
    # Courtesy of https://gist.github.com/deekayen/4148741
    f = open('dictionary.txt')
    wordList = f.read().split()
    for i in range(0, 4):
        word = wordList[i]
        password = password + word
    print(password)
    #print("Macaw!") #DEBUG

main()
