import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)
cahrcters_number = input("how many charcters you want?:\n")

while True:
    try:
        cahrcters_number= int(cahrcters_number)
        if cahrcters_number < 6 :
            print("you need at least 6 charchters")
            cahrcters_number = input ("please enter the number again: \n")
        else:
            break
    except:
        print("please enter numbers only")
        cahrcters_number = input ("please enter the number again: \n")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(cahrcters_number * (30/100))
part2 = round(cahrcters_number * (20/100))

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)

password ="".join(password[0:])

print(password)