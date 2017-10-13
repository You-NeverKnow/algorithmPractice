from hashTable import HashTable

hash_table = HashTable(bucket_count = 50)

x = hash_table.insert(50)
y = hash_table.insert(50)
hash_table.insert(20)

a = hash_table.search(50)
b = hash_table.search(21)
c = hash_table.search(20)
d = hash_table.remove(20)
e = hash_table.search(20)


print(a, b, d, c, e, x, y)