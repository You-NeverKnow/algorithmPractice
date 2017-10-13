# =============================================================================|
class Node:
    """
    Creates nodes for a binary tree
    """
# -----------------------------------------------------------------------------|
    def __init__(self, parent = None, left = None, right = None, value = None):
        """
        Constructor for Node
        """
        self.parent = parent
        self.left = left
        self.right = right

        self.value = value
        self.duplicates = 0
# -----------------------------------------------------------------------------|
#==============================================================================#