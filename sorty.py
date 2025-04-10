import random
import time

def calcList(maxValue, howMany):
    for i in range(howMany):
        myList = []
        number = random.randint(0, maxValue)
        myList.append(number)
        return myList
    
myList = calcList

def linear_search(list, target):
    hits = []
    for i in range(len(list)):
        if list[i] == target:
            hits.append(i)
    return hits

def binary_search(list,targt):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2

        if list[mid] == target:
            return mid
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid + 1
    return -1

target = int(input("What's the number? "))

result = binary_search(myList, target)

if result == -1:
    print(f"{target} not found in the list")
else:
    print(f"{target} found at index {result}")
