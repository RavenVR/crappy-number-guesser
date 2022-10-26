from time import *
import random as r
a1 = open(r"cnf-log.txt", "a")
a = 0
guess = False
num = 0
log = ''
log1=''
def convertTuple(tup):
    log1 = ''.join(tup)
    return log1
mode = input("which mode do you want? (random[r] or normal[n])? ")
mode = mode.lower()
h=False
if mode == "n":

    while True:
        try:
            a = int(input("Please enter a number: "))
            if a < 0:
                a = int(input("Please enter a number: "))
            elif a > 0:
                h = True
                break
        except ValueError:
            print ("Oops!  That was no valid number.  Try again...")
            sleep(1)
    print("guessing the number, it will aprox take: ", a/10000, "seconds.")
    
elif mode == "r":
    a = r.randint(1,600000)
    h = True
else:
    print('please try again!')
    sleep(1)
while h == True:
    time = str(round(a/10000))
    number = str(a)
    if mode == 'r':
        log1 = "The random number: ",number," took: ",time," seconds."
    elif mode == 'n':
        log1 = "The number: ",number," took: ",time," seconds."
    else:
        quit()
    log = convertTuple(log1)
    guess = True
    h = False
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
