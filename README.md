# Algorithms & Data Structures
Implementation of some standard algorithms/DataStructures from [Steven Skienna Algorithm Design Manual book](https://www.amazon.com/Algorithm-Design-Manual-Steven-Skiena/dp/1849967202/)

### Binary Search Tree
A binary search tree is a rooted binary tree, whose internal nodes each store a key (and optionally, an associated value) and each have two distinguished sub-trees, commonly denoted left and right. The tree additionally satisfies the binary search property, which states that the key in each node must be greater than or equal to any key stored in the left sub-tree, and less than or equal to any key stored in the right sub-tree. The leaves (final nodes) of the tree contain no key and have no structure to distinguish them from one another.

| Algorithm  | Average | Worse case |
| ------------- | ------------- | ------------- |
| Search	| O(log n) | O(n) |
| Insert |	O(log n) | O(n) |
| Delete	| O(log n) | O(n) |

### Heap
A heap is a specialized tree-based data structure that satisfies the heap property: if P is a parent node of C, then the key (the value) of P is either greater than or equal to (in a max heap) or less than or equal to (in a min heap) the key of C. The node at the "top" of the heap (with no parents) is called the root node.

| Algorithm |	Average	| Worst case |
| ------------- | ------------- | ------------- |
| Search	|	O(n)	| O(n) |
| Insert	|	O(1)	| O(log n) |
| Delete	|	O(log n)	| O(log n) |
| findMin | O(1) | O(1) |
| Sort | O(nlogn) | O(nlogn) |

### HashMap
A hash map is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

| Algorithm |	Average	| Worst case |
| ------------- | ------------- | ------------- |
| Search	|	O(1)	| O(n) |
| Insert	|	O(1)	| O(n) |
| Delete	|	O(1)	| O(n) |

### Sorting

| Algorithm |	Average	| Worst case |
| ------------- | ------------- | ------------- |
| Selection sort	|	O(n^2)	| O(n^2) |
| Bubble Sort	|	O(n^2)	| O(n^2) |
| Insertion Sort	|	O(n^2)	| O(n^2) |
| Merge Sort	|	O(nlogn)	| O(nlogn) |
| Quick Sort	|	O(nlogn)	| O(n^2) |
