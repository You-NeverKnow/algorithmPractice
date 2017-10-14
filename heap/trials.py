import random
from heap import Heap


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


min_heap = Heap(form = "min")

# trial insert
my_random_list = []
for iteration in range(20000):
    random_number = random.randint(0, 2000)

    min_heap.insert(element = random_number)

    my_random_list.append(random_number)

sorted_list = min_heap.sort()
print("Unsorted List was ", my_random_list)
print("Heap-sorted list = ", sorted_list)
print("Sorting status:", check_sort(my_random_list, sorted_list))

