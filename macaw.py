# Macaw

password = ""
f = open('dictionary.txt')
for word in f.read().split():
    password = password + word

print(password)
