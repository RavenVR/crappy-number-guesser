import random as r
from time import *

a1 = open(r"cnf-log.txt", "r+")

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
log = ["The number: ",number," took: ",time," seconds"]
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
a1.writelines(log)
sleep(5)
