import random
import time


def calc_list(maxValue: int, howMany: int) -> list:
    myList = []
    for i in range(howMany):
        number = random.randint(0, maxValue)
        myList.append(number)

    return myList


nonSortedList = calc_list(10000, 300000)


def selection_sort(listToSort: list)  -> list:
    """Uses selection sort to sort a given list"""
    # Copy the list to a new list and track how long it takes to copy
    start_time_to_copy = time.perf_counter()
    newList = listToSort.copy()
    end_time_to_copy = time.perf_counter()
    elapsed_time_to_copy = end_time_to_copy - start_time_to_copy

    print(f"list took {elapsed_time_to_copy:.6f} seconds to copy")

    # shamelessly stolen from scaler.com, website included an explanation
    for i in range(len(newList)):
        # Set min_index = to first unsorted element
        min_index = i

        start_time = time.perf_counter()
        # Loop to iterate over unsorted sub arrary
        for j in range(i + 1, len(newList)):
            # Finding the minimum element in the unsorted sub-array
            if newList[min_index] > newList[j]:
                min_index = j

        newList[i], newList[min_index] = newList[min_index], newList[i]
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    print(f"List took {end_time:.4f} seconds to sort")

    return newList

testList = selection_sort(nonSortedList)
# print(testList)

def linear_search(listToSort: list, target: int):
    """Given a list, searches it for a given target"""
    hits = []
    for i in range(len(listToSort)):
        if listToSort[i] == target:
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


# target = int(input("What's the number? "))

# result = binary_search(nonSortedList, target)

# if result == -1:
#     print(f"{target} not found in the list")
# else:
#     print(f"{target} found at index {result}")
