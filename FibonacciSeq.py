# name : Samir , @samiro0on , mail: mahmoudsamir109@gmail.com
# Fibonacci series

firstNum = int(input("Please enter the first number of the sequence,,, "))
endNum = int(input("please enter the largest number in the fibonacci sequence,,, "))

def fibonacciSeq(firstNum):

    fibSeries = [firstNum,firstNum]
    n = 2

    while fibSeries[-1] < endNum:
        var = fibSeries[n-1] + fibSeries[n-2]
        fibSeries.append(var)
        n += 1

    if fibSeries[-1] > endNum:
        fibSeries.pop()

    return fibSeries

print(fibonacciSeq(firstNum))
######################################################################################
# another way to write the fibonacci equation in a general way is

# def F(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else:
#     return F(n-1)+F(n-2)

#######################################################################################
# variable series of fibonacci sequence

def myFiboSeq():
    x1 = 0
    x2 = 1
    limit = int(input("please enter the limit of the fibonacci series ... "))
    print(x1)     # if you wanna start with 0 if not comment it ;)
    while x2 < limit:
        print(x2)
        x1, x2 = x2, x1 + x2
# test case
myFiboSeq()
print("Thank You")