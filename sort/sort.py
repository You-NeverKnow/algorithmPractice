import random


# =============================================================================|
class Sort:
    """
    Implements various sorting algorithms
    """
    # -------------------------------------------------------------------------|
    def __int__(self):
        self.array = []

    def bubble_sort(self, some_list):
        """
         Implements bubble sort. O(n**2)
        """
        some_list_copy = some_list[:]
        for index in range(len(some_list_copy)):
            for other_index in range(index + 1, len(some_list_copy)):
                # if smaller, swap
                if some_list_copy[other_index] < some_list_copy[index]:
                    self._swap(some_list_copy, index, other_index)

        return some_list_copy
    # -------------------------------------------------------------------------|

    # -------------------------------------------------------------------------|

    def insertion_sort(self, some_list):
        """
         Implements insertion sort. O(n**2)
        """
        sorted_list = []

        for iteration_number in range(len(some_list)):
            sorted_list.append(some_list[iteration_number])

            current_index = len(sorted_list) - 1
            while current_index > 0:
                current_element = sorted_list[current_index]
                previous_element = sorted_list[current_index - 1]

                if current_element < previous_element:
                    self._swap(sorted_list, current_index, current_index - 1)
                    current_index -= 1
                else:
                    break

        return sorted_list
    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def selection_sort(self, some_list):
        """
        Implements selection sort
        """
        sorted_list = []
        some_list_copy = some_list[:]

        for iteration in range(len(some_list_copy)):
            current_minimum_index = self._get_min_index(some_list_copy)

            sorted_list.append(some_list_copy.pop(current_minimum_index))

        return sorted_list
    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    @staticmethod
    def _get_min_index(some_list):
        """
        returns minimum number's index from a list
        """
        min_index = 0
        minimum = some_list[min_index]

        for index, item in enumerate(some_list):
            if item < minimum:
                minimum = item
                min_index = index

        return min_index
    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def merge_sort(self, some_list):
        """
        Implements merge sort
        """
        if len(some_list) == 1:
            return some_list

        middle = len(some_list)//2

        left = self.merge_sort(some_list[:middle])
        right = self.merge_sort(some_list[middle:])

        return self._merge(sorted_left = left, sorted_right = right)
    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def quick_sort(self, some_list):
        """
        Implements quick-sort
        """
        if len(some_list) <= 1:
            return some_list

        get_random_index = random.randint(0, len(some_list) - 1)
        selected_element = some_list[get_random_index]

        less_than_index = []
        greater_than_index = []
        equal_to_index = []

        for element_index, element in enumerate(some_list):

            if element < selected_element:
                less_than_index.append(element)
            elif element > selected_element:
                greater_than_index.append(element)
            else:
                equal_to_index.append(element)

        return self.quick_sort(less_than_index) + \
               equal_to_index + \
               self.quick_sort(greater_than_index)

    # -------------------------------------------------------------------------|

    # -------------------------------------------------------------------------|

    @staticmethod
    def _merge(sorted_left, sorted_right):
        """

        """
        merged_sorted_list = []

        while len(sorted_left) != 0 and len(sorted_right) != 0:
            if sorted_left[0] < sorted_right[0]:
                merged_sorted_list.append(sorted_left.pop(0))
            elif sorted_right[0] < sorted_left[0]:
                merged_sorted_list.append(sorted_right.pop(0))
            else:
                merged_sorted_list.append(sorted_right.pop(0))
                merged_sorted_list.append(sorted_left.pop(0))

        merged_sorted_list = merged_sorted_list + sorted_left + sorted_right

        return merged_sorted_list
    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    @staticmethod
    def _swap(some_array, index1, index2):
        """
        swaps two elements of an array
        """
        some_array[index1], some_array[index2] =\
            some_array[index2], some_array[index1]

    # -------------------------------------------------------------------------|

# =============================================================================|
