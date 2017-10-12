from node import Node

# ============================================================================ |
class BinaryTree():
    """
    Implements a Binary tree.
    """

    # -------------------------------------------------------------------------|
    def __init__(self, head):
        """
        Constructor for BinaryTree
        """
        self.head = head

    # -------------------------------------------------------------------------|

    # -------------------------------------------------------------------------|

    def insert(self, new_node):
        """
        Inserts a node into the Binary tree.
        """
        new_value = new_node.value

        # Find position in tree
        parent = self._search(new_value)
        new_node.parent = parent

        # Place to the left or right or at the same position depending on value
        if parent.value > new_value:
            parent.left = new_node
        elif parent.value < new_value:
            parent.right = new_node
        else:
            parent.duplicates += 1

    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def remove(self, value):
        """
        Removes an element from the tree.
        """

        node_to_be_removed = self.search(value = value)

        # If node is not present in tree
        if node_to_be_removed is None:
            return False

        # If node position has multiple values, simply decrement count
        if node_to_be_removed.duplicates > 0:
            node_to_be_removed.duplicates -= 1
            return True

        # if node to be removed is root
        is_head = self.head.value == node_to_be_removed.value
        has_left = self.head.left is not None
        has_right = self.head.right is not None

        if is_head:
            if not has_left and not has_right:
                self.head.value = None
            elif not has_left and has_right:
                self.head = self.head.right
            elif has_left and not has_right:
                self.head = self.head.left
            else:
                right_binary_tree = BinaryTree(head = self.head.right)
                right_binary_tree.insert(new_node = self.head.left)
                self.head = self.head.right

            return True

        # else, check which side of parent is to be removed, and remove it
        parent = node_to_be_removed.parent

        remove_left = parent.value > node_to_be_removed.value
        had_left_child = node_to_be_removed.left is not None
        had_right_child = node_to_be_removed.right is not None

        if remove_left and not had_left_child and not had_right_child:
            parent.left = None
        elif remove_left and had_left_child and not had_right_child:
            parent.left = node_to_be_removed.left
        elif remove_left and not had_left_child and had_right_child:
            parent.left = node_to_be_removed.right
        elif remove_left and had_left_child and had_right_child:
            parent.left = node_to_be_removed.right
            right_binary_tree = BinaryTree(head = node_to_be_removed.right)
            right_binary_tree.insert(node_to_be_removed.left)

        elif not remove_left and not had_left_child and not had_right_child:
            parent.right = None
        elif not remove_left and had_left_child and not had_right_child:
            parent.right = node_to_be_removed.left
        elif not remove_left and not had_left_child and had_right_child:
            parent.right = node_to_be_removed.right
        else:
            parent.right = node_to_be_removed.left
            left_binary_tree = BinaryTree(head = node_to_be_removed.left)
            left_binary_tree.insert(node_to_be_removed.right)

        return True

    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def search(self, value):
        """
        Searches for a value, and returns True/False depending on whether it is
        present or not.
        """
        lastNode = self._search(value = value)

        if lastNode.value == value:
            return lastNode
        else:
            return None
    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|    
    
    def is_present(self, value):
        """
        Checks if a value is present inside the tree or not
        """
        search_result = self.search(value = value)

        if search_result is None:
            return False
        else:
            return True
    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def _search(self, value):
        """
        Searches for a value in the tree
        """

        # Larger values go to the right

        if self.head.value < value:
            if self.head.right is None:
                return self.head
            else:
                right__binary_tree = BinaryTree(head = self.head.right)
                return right__binary_tree._search(value = value)

        # Smaller values go to the left
        if self.head.value > value:
            if self.head.left is None:
                return self.head
            else:
                left__binary_tree = BinaryTree(head = self.head.left)
                return left__binary_tree._search(value = value)

        # Equal values stay in the same spot
        return self.head

    # -------------------------------------------------------------------------|

    # -------------------------------------------------------------------------|

    def sort(self):
        """
         Returns a list containing sorted elements of the Binary tree.

         Divide trees into sub-trees, and append sorted lists of all to get
         final sorted list

        """
        sorted_list = []

        # sorted list from left side
        if self.head.left is not None:
            left__binary_tree = BinaryTree(head = self.head.left)
            sorted_list += left__binary_tree.sort()

        # account for duplicates as well
        for count in range(self.head.duplicates + 1):
            sorted_list.append(self.head.value)

        # sorted list from right side
        if self.head.right is not None:
            right__binary_tree = BinaryTree(head = self.head.right)
            sorted_list += right__binary_tree.sort()

        return sorted_list
    # -------------------------------------------------------------------------|

# ============================================================================ |
