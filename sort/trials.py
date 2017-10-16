# -----------------------------------------------------------------------------|
import random

import time

import sort

# -----------------------------------------------------------------------------|
def check_sort(some_list, my_sorted_list):
    """
    Checks whether the sorting algorithm correctly sorts a random list in
    ascending order
    """

    for each_element in some_list:
        if each_element not in my_sorted_list:
            return False

    for index in range(len(my_sorted_list) - 1):
        if my_sorted_list[index] > my_sorted_list[index + 1]:
            return False

    return True
# -----------------------------------------------------------------------------|
# -----------------------------------------------------------------------------|
def list_is_same(some_list, other_list):
    """
    Checks if a list is same as other
    """
    return some_list == other_list
# -----------------------------------------------------------------------------|


# Create random list
some_random_list = []
my_sort = sort.Sort()

for iteration in range(20000):
    random_number = random.randint(0, 2000)
    some_random_list.append(random_number)

my_random_list = some_random_list[:]
print("List was", my_random_list)

# ---------------------------------------------------------------------------- #
# Insertion sort test
# ---------------------------------------------------------------------------- #
start = time.time()
my_sorted_list = my_sort.insertion_sort(my_random_list)
end = time.time()

print("Insertion sorted list = ", my_sorted_list)
print("Sorting status:", check_sort(my_random_list, my_sorted_list))
print("Didn't change unsorted list =", list_is_same(my_random_list,
                                                    some_random_list))
print("Times taken = ", end - start, "seconds")
print("\n")
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# Quick-sort test
# ---------------------------------------------------------------------------- #

start = time.time()
my_sorted_list = my_sort.quick_sort(my_random_list)
end = time.time()

print("Quick sorted list = ", my_sorted_list)
print("Sorting status:", check_sort(my_random_list, my_sorted_list))
print("Didn't change unsorted list =", list_is_same(my_random_list,
                                                    some_random_list))
print("Times taken = ", end - start, "seconds")

print("\n")
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# Merge sort test
# ---------------------------------------------------------------------------- #
start = time.time()
my_sorted_list = my_sort.merge_sort(my_random_list)
end = time.time()

print("Merge sorted list = ", my_sorted_list)
print("Sorting status:", check_sort(my_random_list, my_sorted_list))
print("Didn't change unsorted list =", list_is_same(my_random_list,
                                                    some_random_list))
print("Times taken = ", end - start, "seconds")

print("\n")
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
# Selection sort test
# ---------------------------------------------------------------------------- #
start = time.time()
my_sorted_list = my_sort.selection_sort(my_random_list)
end = time.time()

print("Selection sorted list = ", my_sorted_list)
print("Sorting status:", check_sort(my_random_list, my_sorted_list))
print("Didn't change unsorted list =", list_is_same(my_random_list,
                                                    some_random_list))
print("Times taken = ", end - start, "seconds")

print("\n")
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# Bubble sort test
# ---------------------------------------------------------------------------- #
start = time.time()
my_sorted_list = my_sort.bubble_sort(my_random_list)
end = time.time()

print("Bubble sorted list = ", my_sorted_list)
print("Sorting status:", check_sort(my_random_list, my_sorted_list))
print("Didn't change unsorted list =", list_is_same(my_random_list,
                                                    some_random_list))
print("Times taken = ", end - start, "seconds")

print("\n")

# ---------------------------------------------------------------------------- #

