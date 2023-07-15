from random import randrange, shuffle

"""
Quicksort is a method for sorting an array by repeatedly partitioning it into sub-arrays by:
    - Selecting an element from the current array. This element is called the pivot element, and in our implementation we used the mid element.
    - Comparing every element in the array to the pivot element, swap the elements into sides greater than and less than. The partition point in the array is where we guarantee everything before is less and everything after is greater than.
    - Repeating this process on the sub-arrays separated by the partition point. Do this until a sub-array contains a single element. When the partitioning and swapping are done, the arrays are sorted from smallest to largest.

Time Complexity: The worst case runtime for quicksort is O(N^2) and the average runtime for quicksort is O(N logN). The worst case runtime is so unusual that the quicksort algorithm is typically referred to as O(N logN)
Space Complexity: O(log N)
"""


def quicksort(list, start, end):
    # this portion of list has been sorted
    if start >= end:
        return
    print("Running quicksort on {0}".format(list[start: end + 1]))
    # select random element to be pivot
    pivot_idx = randrange(start, end + 1)
    pivot_element = list[pivot_idx]
    print("Selected pivot {0}".format(pivot_element))
    # swap random element with last element in sub-lists
    list[end], list[pivot_idx] = list[pivot_idx], list[end]

    # tracks all elements which should be to left (lesser than) pivot
    less_than_pointer = start

    for i in range(start, end):
        # we found an element out of place
        if list[i] < pivot_element:
            # swap element to the right-most portion of lesser elements
            print("Swapping {0} with {1}".format(
                list[i], list[less_than_pointer]))
            list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
            # tally that we have one more lesser element
            less_than_pointer += 1
    # move pivot element to the right-most portion of lesser elements
    list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
    print("{0} successfully partitioned".format(list[start: end + 1]))
    # recursively sort left and right sub-lists
    quicksort(list, start, less_than_pointer - 1)
    quicksort(list, less_than_pointer + 1, end)


list = [5, 3, 1, 7, 4, 6, 2, 8]
shuffle(list)
print("PRE SORT: ", list)
print(quicksort(list, 0, len(list) - 1))
print("POST SORT: ", list)
