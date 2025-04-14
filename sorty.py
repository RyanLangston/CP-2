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


def selection_sort(listToSort: list):
    """Uses selection sort to sort a given list"""
    newList = listToSort.copy()

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

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    # print(f"List took {elapsed_time:.4f} seconds to sort")

    # TODO: Might need to return two variables, newList and elapsed_time
    return newList, elapsed_time


def insertion_sort(listToSort: list):
    arr = listToSort.copy()
    n = len(arr)

    start_time = time.perf_counter()
    if n <= 1:
        return arr  # List would already be sorted

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Shift elements to the left
            j -= 1
        arr[j + 1] = key

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"List took {elapsed_time:.4f} seconds to sort")
    # TODO: Might need to return two variables, newList and elapsed_time
    return arr, elapsed_time


def quicksort(listToSort):
    # Now I had to learn about inner functions but I'm pretty sure I understnad it
    start_time = time.perf_counter()

    # Actual function is a inner function prefixed with _ to indicate that it shouldn't be called directly
    def _quicksort(sublist):
        if len(sublist) <= 1:
            return sublist

        # We go ahead use list comprehension as its slightly faster (not enough to affect results) and is considered my pythonic
        pivot = sublist[len(sublist) // 2]
        left = [x for x in sublist if x < pivot]
        middle = [x for x in sublist if x == pivot]
        right = [x for x in sublist if x > pivot]

        return _quicksort(left) + middle + _quicksort(right)

    sortedList = _quicksort(listToSort.copy())

    elapsed_time = time.perf_counter() - start_time

    return sortedList, elapsed_time


def linear_search(listToSort, target):
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


def run_speed_tests():
    """Runs the speed tests"""
    original_list = calc_list(10000, 100000)
    print("List has been created")
    target = 3231

    # Create 5 seperate copies
    list1 = original_list.copy()  # For unsorted linear search
    list2 = original_list.copy()  # For sorted linear search
    list3 = original_list.copy()  # For selection sort + binary search
    list4 = original_list.copy()  # For insertion sort + binary search
    list5 = original_list.copy()  # For quicksort + binary search

    # This stuff below is AI, I was lazy and didn't want to type all the print statements manually
    # Step 8: Unsorted linear search
    print("\nRunning unsorted linear search...")
    _, unsorted_linear_time = linear_search(list1, target)

    # Step 9: Sorted linear search
    print("\nRunning selection sort then linear search...")
    sorted_list2, selection_sort_time = selection_sort(list2)
    _, sorted_linear_time = linear_search(sorted_list2, target)
    selection_then_linear_time = selection_sort_time + sorted_linear_time

    # Step 10: Selection sort + binary search
    print("\nRunning selection sort then binary search...")
    sorted_list3, selection_sort_time = selection_sort(list3)
    _, binary_time = binary_search(sorted_list3, target)
    selection_then_binary_time = selection_sort_time + binary_time

    # Step 11: Insertion sort + binary search
    print("\nRunning insertion sort then binary search...")
    sorted_list4, insertion_sort_time = insertion_sort(list4)
    _, binary_time = binary_search(sorted_list4, target)
    insertion_then_binary_time = insertion_sort_time + binary_time

    # Step 12: Quicksort + binary search
    print("\nRunning quicksort then binary search...")
    sorted_list5, quicksort_time = quicksort(list5)
    _, binary_time = binary_search(sorted_list5, target)
    quicksort_then_binary_time = quicksort_time + binary_time

    # Print report
    print("\n--- SPEED TEST REPORT ---")
    print(f"Unsorted Linear Search time: {unsorted_linear_time * 1000:.2f}ms")
    print(f"Sorted Linear Search time: {selection_then_linear_time * 1000:.2f}ms")
    print(
        f"Selection Sort then Binary Search time: {selection_then_binary_time * 1000:.2f}ms"
    )
    print(
        f"Insertion Sort then Binary Search time: {insertion_then_binary_time * 1000:.2f}ms"
    )
    print(
        f"Custom Sort (Quicksort) then Binary Search time: {quicksort_then_binary_time * 1000:.2f}ms"
    )


run_speed_tests()
