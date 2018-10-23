print("Macaw!")
f = open('dictionary.txt')
for word in f.read().split():
    print(word)
