import random

from binaryTree import BinaryTree
from node import Node

head_value = 15
head_node = Node(value = head_value)
binary_tree = BinaryTree(head = head_node)

my_randon_list = [head_value]

for iteration in range(10):
    random_number = random.randint(0, 30)
    binary_tree.insert(new_value = random_number)
    my_randon_list.append(random_number)

print("List was", my_randon_list)
print("Sorted List", binary_tree.sort())


