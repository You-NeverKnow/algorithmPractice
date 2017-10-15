import random

# =============================================================================|
class Sort:
    """
    Implements various sorting algorithms
    """
    # -------------------------------------------------------------------------|
    def bubble_sort(self, some_list):
        """
         Implements bubble sort. O(n**2)
        """
        for index in range(len(some_list)):
            for other_index in range(index + 1, len(some_list)):
                # if smaller, swap
                if some_list[other_index] < some_list[index]:
                    self._swap(some_list, index, other_index)

        return some_list
    # -------------------------------------------------------------------------|

    # -------------------------------------------------------------------------|

    def insertion_sort(self, some_list):
        """
         Implements insertion sort. O(n**2)
        """
        for iteration_number in range(1, len(some_list)):
            current_index = iteration_number
            while (current_index > 0) or \
                        some_list[current_index] < some_list[current_index - 1]:

                self._swap(some_list, current_index - 1, current_index)
                current_index -= 1

        return some_list
    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def selection_sort(self, some_list):
        """
        Implements selection sort
        """
        sorted_list = []
        some_list_copy = some_list[:]

        for iteration in range(len(some_list_copy)):
            current_minimum = min(some_list_copy)
            some_list.append(current_minimum)

        return sorted_list
    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def merge_sort(self, some_list):
        """
        Implements merge sort
        """
        middle = int(len(some_list)/2)
        return self._merge(self.merge_sort(some_list[:middle]),
                           self.merge_sort(some_list[middle:]))
    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def quick_sort(self, some_list):
        """
        Implements quick-sort
        """
        if len(some_list == 1):
            return some_list

        get_random_index = random.randint(len(some_list))
        selected_element = some_list[get_random_index]

        less_than_index = []
        greater_than_index = []
        equal_to_index = []

        for element_index, element in enumerate(some_list):
            if element_index == get_random_index:
                continue

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
    def _merge(some_list, other_list):
        """

        """
        merged_sorted_list = []

        while len(some_list) != 0 or len(other_list) != 0:
            if some_list[0] < other_list[0]:
                merged_sorted_list.append(some_list.pop(0))
            elif other_list[0] < some_list[0]:
                merged_sorted_list.append(other_list.pop(0))
            else:
                merged_sorted_list.append(other_list.pop(0))
                merged_sorted_list.append(some_list.pop(0))

        merged_sorted_list = merged_sorted_list + some_list + other_list

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
