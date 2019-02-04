# name : Samir , @samiro0on , mail: mahmoudsamir109@gmail.com
# binary search 16/1/2019  , divide and conquer

import random
def sortedList (size = 10, max = 100):
    sortedArray = []
    for nTimes in range(0,size):
        sortedArray.append(random.randrange(0,max,1))
    sortedArray.sort()
    return sortedArray
# print(sortedList())

def BinarySearch (sortedArray , goal):

    if len(sortedArray) == 0 or len(sortedArray) == 1 and sortedArray[0] != goal :
        return False

    middleIndex = int(len(sortedArray)/2)
    middleValue = sortedArray[middleIndex]

    if middleValue == goal :
        location = middleIndex
        return True
    if middleValue > goal :
        return BinarySearch(sortedArray[:middleIndex], goal)
    if middleValue < goal :
        return BinarySearch(sortedArray[middleIndex:],goal)


var = sortedList(20,25)
print(var)
print("Did y find yr target = ", BinarySearch(var, goal=23))

# binary search tree
def binarySearch(array, left, right, target):
    # Check base case
    if right >= left:
        mid = int(left + (right - left) / 2)

        # If element is present at the middle itself
        if array[mid] == target:
            return mid
            # If element is smaller than mid, then it
        # can only be present in left subarray
        elif array[mid] > target:
            return binarySearch(array, left, mid - 1, target)
        elif array[mid] < target:
            return binarySearch(array, mid + 1, right, target)
        else:
        # Element is not present in the array
            return -1

# Test case
arr = [2, 3, 4, 10, 23, 40, 70]
goal = 10
# Function call

location = binarySearch(arr, 0, (len(arr) - 1), goal)
if location != -1:
    print("Element is present at index % d" % location)
else:
    print("Element is not present in array")


