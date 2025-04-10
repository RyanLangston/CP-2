import random
import time


def calc_list(maxValue: int, howMany: int) -> list:
    for i in range(howMany):
        myList = []
        number = random.randint(0, maxValue)
        myList.append(number)
        return myList


nonSortedList = calc_list(8192, 3000)


def selection_sort(listToSort: list):
    # Copy the list to a new list
    newList = listToSort.copy()
    """Uses selection sort to sort a given list"""
    # shamelessly stolen from scaler.com, website included an explanation
    for i in range(len(newList)):
        # Set min_index = to first unsorted element
        min_index = i

        # Loop to iterate over unsorted sub arrary
        for j in range(i + 1, len(newList)):
            # Finding the minimum element in the unsorted sub-array
            if newList[min_index] > newList[j]:
                min_index = j

        newList[i], newList[min_index] = newList[min_index], newList[i]

        # DEBUG: Following line is to be removed at a later date and is meant to be temp
        print(newList)

        return newList


def linear_search(list, target):
    hits = []
    for i in range(len(list)):
        if list[i] == target:
            hits.append(i)
    return hits


def binary_search(list, targt):
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

result = binary_search(nonSortedList, target)

if result == -1:
    print(f"{target} not found in the list")
else:
    print(f"{target} found at index {result}")
