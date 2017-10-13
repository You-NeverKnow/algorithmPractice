# =============================================================================|
class HashTable:
    """
    Implements a hash table data structure
    """

    # -------------------------------------------------------------------------|
    def __init__(self, bucket_count):
        """
        Constructor for HashTable
        """
        self._count = 0
        self.bucket_count = bucket_count
        self.table = [[] for x in range(self.bucket_count)]
    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def get_hash_number(self, item):
        """
         returns a number based on a string
        """
        string_representation_item = item.__str__()

        number = 0
        for letterIndex, letter in enumerate(string_representation_item):
            number += letterIndex + (letterIndex * ord(letter))

        return number % self.bucket_count

    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def __len__(self):
        """
         Returns number of elements stored in the table
        """
        return self._count

    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def search(self, item):
        """
        Searches for existence of an item in the table
        """
        hash_number = self.get_hash_number(item)

        presence = item in self.table[hash_number]

        return presence
    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def insert(self, item):
        """
        Generates a hash function based on native __str__ function if item
        """
        hash_number = self.get_hash_number(item = item)

        # This implementation does not allow duplicates
        if item not in self.table[hash_number]:
            self.table[hash_number].append(item)
            self._count += 1
            return True

        return False
    # -------------------------------------------------------------------------|
    # -------------------------------------------------------------------------|

    def remove(self, item):
        """
        Removes an item from hash table
        """
        hash_number = self.get_hash_number(item = item)

        # This implementation does not allow duplicates
        try:
            self.table[hash_number].remove(item)
            self._count -= 1
            return True
        except ValueError:
            return False
    # -------------------------------------------------------------------------|
# ============================================================================ #
