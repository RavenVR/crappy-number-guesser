import random as r
from time import *

def convertTuple(tup):
    log1 = ''.join(tup)
    return log1

a1 = open(r"cnf-log.txt", "a")

while True:
    try:
        a = int(input("Please enter a number: "))
        if a < 0:
            a = int(input("Please enter a number: "))
        elif a > 0:
            break
    except ValueError:
        print ("Oops!  That was no valid number.  Try again...")
        sleep(2)
    

print("guessing the number, it will aprox take: ", a/10000, "seconds.")
time = str(a/10000)
number = str(a)
log1 = "The number: ",number," took: ",time," seconds."
log = convertTuple(log1)
guess = True
num = 0
while guess == True:
    
    num += 1
    num = round(num)
    print("\r", num, end='')
    if num == a:
        guess = False
        break

print("\rthe number was: ", num)
a1.write(log + "\n")
sleep(5)
