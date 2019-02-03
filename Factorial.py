# name : Samir , @samiro0on , mail: mahmoudsamir109@gmail.com
# Factorial in a recursive way

def getFactorial(n):
    if n < 2:
        return 1
    else:
        return n*getFactorial(n-1)

print(getFactorial(int(input("please enter the number you want to factorize it ... "))))

# how to generate a random list of number within a range
import random

def randomList (size = 10, max = 100):
    unsortedList = []
    for xTimes in range(0,size):
        unsortedList.append(random.randrange(0,max,1))
    return unsortedList
print("The random list defaulted size of 10 and max value of a num = 100 is : ", randomList())