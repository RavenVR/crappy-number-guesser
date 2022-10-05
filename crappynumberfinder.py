from time import *


w = False
a = int(input("Please input any number "))
w = False
if a < 0:
    w = True
while w == True:
    if a < 0:
        a = int(input("Please input any number "))
    elif a > 0:
        w = False
        break

print("guessing the number, it will aprox take: ", a/10000, "seconds.")
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

sleep(5)
