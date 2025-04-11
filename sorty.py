import random
import time


def calc_list(maxValue: int, howMany: int) -> list:
    myList = []
    for i in range(howMany):
        number = random.randint(0, maxValue)
        myList.append(number)

    return myList


# This list should never be sorted inplace
original_list = calc_list(10000, 10000)


def selection_sort(listToSort: list) -> list:
    """Uses selection sort to sort a given list"""
    # Copy the list to a new list and track how long it takes to copy
    start_time_to_copy = time.perf_counter()
    newList = listToSort.copy()
    end_time_to_copy = time.perf_counter()
    elapsed_time_to_copy = end_time_to_copy - start_time_to_copy

    print(f"list took {elapsed_time_to_copy:.6f} seconds to copy")

    # Initialize counter before starting the sort
    iteration_counter = 0
    # Start timing the sort process
    start_time = time.perf_counter()

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
        iteration_counter += 1
        print(iteration_counter)

    end_time = time.perf_counter()
    print(f"Total iterations: {iteration_counter}")

    elapsed_time = end_time - start_time
    print(f"List took {elapsed_time:.4f} seconds to sort")

    return newList


def insertion_sort():
    pass


testList = selection_sort(original_list)
# print(testList)


def linear_search(listToSort: list, target: int):
    """Given a list, searches it for a given target"""
    hits = []
    for i in range(len(listToSort)):
        if listToSort[i] == target:
            hits.append(i)
    return hits


def binary_search(list, target):
    left = 0
    right = len(list) - 1
    hits = []

    # First, find any occurrence
    while left <= right:
        mid = (left + right) // 2

        if list[mid] == target:
            # Found one occurrence, now check for others
            hits.append(mid)

            # Check to the left
            temp_left = mid - 1
            while temp_left >= 0 and list[temp_left] == target:
                hits.append(temp_left)
                temp_left -= 1

            # Check to the right
            temp_right = mid + 1
            while temp_right < len(list) and list[temp_right] == target:
                hits.append(temp_right)
                temp_right += 1

            return sorted(hits)  # Return sorted indices
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return hits  # Return empty list if not found


# target = int(input("What's the number? "))

# result = binary_search(nonSortedList, target)

# if result == -1:
#     print(f"{target} not found in the list")
# else:
#     print(f"{target} found at index {result}")
