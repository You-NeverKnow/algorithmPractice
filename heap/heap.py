# =============================================================================|
class Heap:
    """
    Creates Heap data structures
    """
    # -------------------------------------------------------------------------|

    def __init__(self, form):
        """
        Constructor for Heap

        :param  form Takes either "min" or "max" values to evaluate dominant
                        node
        """
        assert form == "min" or form == "max"

        self._type = form
        self.array = []

    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def insert(self, element):
        """
        adds an element to the heap
        """
        self.array.append(element)

        self._bubble_up(child_index = len(self.array) - 1)

    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|    
    
    def pop_head(self):
        """
        Removes the most dominant node from the heap
        """
        head = self.array[0]

        # Replace head with a new element from the heap
        if len(self.array) > 1:
            self.array[0] = self.array.pop()
        self._bubble_down(parent_index = 0)

        return head

    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def sort(self):
        """
        Implements heap-sort. Continuously pops the most dominant node, which is
        guaranteed to be larger than or equal to, or smaller than equal to all
        other elements in the heap, thus creating a sorted list.

        """
        sorted_array = []

        # Preserve the state of the heap
        temp_array = self.array[:]

        # create sorted array with selection sort(selection is easy.
        # It is always the head node.
        for iteration in range(len(self.array)):
            sorted_array.append(self.pop_head())

        # restore the state of the heap
        self.array = temp_array[:]

        return sorted_array
    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def _bubble_down(self, parent_index):
        """
        Bubbles an unfit parent down the heap
        """
        son_index, daughter_index = self._get_child_indices(parent_index)

        # Exit condition: Reached bottom of the heap
        if son_index >= len(self.array):
            return

        if daughter_index >= len(self.array):
            family_indices = parent_index, son_index
        else:
            family_indices = parent_index, son_index, daughter_index

        dominant_index = self._get_dominant(family_indices)

        if dominant_index == parent_index:
            return

        else:
            self._swap_elements(parent_index, dominant_index)
            self._bubble_down(dominant_index)

    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def _get_dominant(self, family_indices):
        """
        Returns the most dominant member among parent and its two child nodes
        """
        family = [self.array[x] for x in family_indices]

        if self._type == 'min':
            dominant = min(family)
        else:
            dominant = max(family)

        for index in family_indices:
            if self.array[index] == dominant:
                return index

    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    @staticmethod
    def _get_child_indices(parent_index):
        """
        returns child indices for a parent
        """
        parent_index += 1

        son_index = 2 * parent_index
        daughter_index = 2 * parent_index + 1

        son_index -= 1
        daughter_index -= 1

        return son_index, daughter_index

    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def _bubble_up(self, child_index):
        """
        Bubbles a genius child up the heap
        """

        if child_index == 0:
            return

        child = self.array[child_index]

        parent_index = self._get_parent_index(child_index)

        parent = self.array[parent_index]

        if self._type == 'min':
            if child <= parent:
                self._swap_elements(child_index, parent_index)
                return self._bubble_up(parent_index)

        if self._type == 'max':

            if child >= parent:
                self._swap_elements(child_index, parent_index)
                return self._bubble_up(parent_index)

    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    @staticmethod
    def _get_parent_index(child_index):
        """
        finds the parent for a child node
        """
        child_index += 1

        # children of kth element = 2k, 2k + 1
        if child_index % 2 == 0:
            parent_index = child_index / 2
        else:
            parent_index = (child_index - 1) / 2

        return int(parent_index - 1)

    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def _swap_elements(self, child_index, parent_index):
        """
        swaps position of child and parent
        """
        self.array[parent_index], self.array[child_index] =\
            self.array[child_index], self.array[parent_index]

    # -------------------------------------------------------------------------|
# =============================================================================|
