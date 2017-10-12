import random

from binaryTree import BinaryTree
from node import Node

# -----------------------------------------------------------------------------|
def check_sort(some_list, sorted_list):
    """

    """

    for each_element in some_list:
        if each_element not in sorted_list:
            return False

    for index in range(len(sorted_list) - 1):
        if sorted_list[index] > sorted_list[index + 1]:
            return False

    return True
# -----------------------------------------------------------------------------|



head_value = 15
head_node = Node(value = head_value)
binary_tree = BinaryTree(head = head_node)

my_random_list = [head_value]

# trial insert
for iteration in range(10):
    random_number = random.randint(0, 30)
    new_node = Node(value = random_number)
    binary_tree.insert(new_node = new_node)
    my_random_list.append(random_number)

print("List was", my_random_list)
print("Sorted List", binary_tree.sort())
print("Sorting status: ", check_sort(my_random_list, binary_tree.sort()))

my_random_list.remove(15)
print("Removed 15 = ", binary_tree.remove(15))
print("Sorted List after removal is", binary_tree.sort())
print("Sorting status: ", check_sort(my_random_list, binary_tree.sort()))

