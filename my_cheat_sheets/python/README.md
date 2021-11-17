# Python cheatsheet

## Data structures
All this content is based on the SoloLearn [Python Data Structures](https://www.sololearn.com/learning/1159) course.
### Working with strings

* count(str) returns how many times the str substring appears in the given string.
* upper() converts the string to uppercase.
* lower() converts the string to lowercase.
* replace(old, new) replaces all occurrences of old with new.
len(str) returns the length of the string (number of characters).

* f-String
```python
name = "Rami"
print(f"Hello {name}") # output: Hello Rami
```
* join method
```python
list_of_strings = ["Hello", "my", "friend"]
my_string_joined = " ".join(list_of_strings) # output: Hello my friend
```


### Working with lists
> Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.

#### List manipulations
* append(item) adds an item to the end of the list.
* insert(index, item) adds an item at the given index in the list.
* remove(item) removes an item from the list.
* pop(index) removes the item at the given index.
* count(item) returns a count of how many times an item occurs in the list.

#### List operations
* reverse() reverses items in the list.
* sort() sorts the list. By default, the list is sorted ascending. You can  specify reverse=True as the parameter, to sort descending.
* max(list) returns the maximum value.
* min(list) returns the minimum value.

#### List comprehensions

* Example. Create cubes of these numbers: 0, 1, 2, 3, 4
```python
cubes = [i**3 for i in range(5)]
print(cubes) # output: [0, 1, 8, 27, 64]
```
* A list comprehension can also contain an if statement to enforce a condition on values in the list.
```python
evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens) # output: [0, 4, 16, 36, 64]
```

#### Useful functions
* enumerate(lista_data): Getting the index and the number of a list
```python
data = [1, 2, 5, 6, 7]
for idx, num in enumerate(data):
    do_something(idx, num)
```

* sorted(list_data): Getting list sorted
```python
data = [1, 2, 5, 6, 7]
sorted_list = sorted(data, reverse=True) # reverse is by default False.
```
* set(data): making our list data unique. the results will be a set data type
```python
data = [1, 1, 2, 2, 5, 6, 7, 7]
unique_set = set(data) # <class 'set'>
```
* counter numbers in a list
```python
from collections import Counter
data = [1, 1, 2, 2, 5, 6, 7, 7, 7]
counts = Counter(data) # output: {1:2, 2:2, 5:1, 6:1, 7:3}
# check most_common instance function
```

### Working with dictionaries
>  Use a dictionary, when you need a logical association between a key:value


* get function
```python
pairs = {
      1: "apple",
      "orange": [2, 3, 4],
      True: False,
      12: "True",
    }
print(pairs.get("orange"))  # output: [2, 3, 4]
print(pairs.get(7, 42))  # output: 42
print(pairs.get(12345, "not found"))  # output: not found
print(pairs["this-key-does-not-exist"])  # KeyError exception
```
* set a default key in a dictionary if it does not exist
```python
my_dict={'name': 'John', 'age': 23}
count=my_dict.setdefault("count", 0)
print(my_dict) # output: {'name': 'John', 'age': 23, 'count': 0}
```
* sorted(dict_data): Getting a dictionary sorted by a key using lambda function as well
```python
my_dict = [
    {"name": "John", "age": 24},
    {"name": "Pepe", "age": 26},
]
sorted_dict = sorted(my_dict, key = lambda x: x["age"])
```
* merge dicts
```python
d1 = {"name": "Pepe", "age": 23}
d2 = {"name": "Pepe", "city": "Madrid"}
d = {**d1, **d2} # d -> {"name": "Pepe", "age": 23, "city": "Madrid"}
```


### Working with tupples
> - Use tuples when your data cannot/should not change.

Tuples are very similar to lists, except that they are immutable (they cannot be changed).
* TypeError
```python
words = ("spam", "eggs", "sausages",)
words[1] = "cheese" # TypeError: 'tuple' object does not support item assignment
```
* An advantage of tuples over lists is that they can be used as keys for dictionaries (because they are immutable):
```python
dict = {
    ("David", 42): "red",
    ("Bob", 24): "green"
}
print(dict[("Bob", 24)]) # output: green
```
* Unpacking
```python
numbers = (1, 2, 3)
a, b, c = numbers
print(a) # output: 1
print(b) # output: 2
print(c) # output: 3
```
* Asterisk (*)
```python
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a) # output: 1
print(b) # output: 2
print(c) # output: [3, 4, 5, 6, 7, 8]
print(d) # output: 9
```
* For generating numbers it is better to use tupples than lists -> memory savings
```python
my_numbers = (i for i in range(100))
```

### Working with sets
> Use a set if you need uniqueness for the elements.

Sets are collections of unordered items that are unique.
* Sets cannot contain duplicate elements
```python
num_set = {1, 2, 3, 3, 4, 4, 5}
print(num_set) # output: {1, 2, 3, 4, 5}
```
* add function: add new items to the set
* remove function: delete a specific element

Sets can be combined using mathematical operations.
* The union operator | combines two sets to form a new one containing items in either.
* The intersection operator & gets items only in both.
* The difference operator - gets items in the first set but not in the second.
* The symmetric difference operator ^ gets items in either set, but not both.
```python
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
print(first | second) # output: {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(first & second) # output: {4, 5, 6}
print(first - second) # output: {1, 2, 3}
print(second - first) # output: {8, 9, 7}
print(first ^ second) # output: {1, 2, 3, 7, 8, 9}
```

### Stacks
> A stack can be implemented using a list in Python.

A stack is a simple data structure that adds and removes elements in a particular order.

Every time an element is added, it goes on the "top" of the stack. Only an element at the top of the stack can be removed, just like a stack of plates. This behavior is called LIFO (Last In, First Out).

```python
class Stack:
    def __init__(self):
        self.items = []  

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def print_stack(self):
        print(self.items)

s = Stack()
s.push('a')
s.push('b')
s.push('c')
s.print_stack() # output: ['c', 'b', 'a']

s.pop()
s.print_stack() # output: ['b', 'a']
```

### Queue
> Python lists are the easiest way to implement a queue functionality.

A queue is similar to a stack, but defines a different way to add and remover elements.
The elements are inserted from one end, called the rear, and deleted from the other end, called the front.
This behavior is called FIFO (First in First Out).


```python
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def print_queue(self):
        print(self.items)

q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('42')
q.print_queue() # output: ['42', 'b', 'a']

q.dequeue()
q.print_queue() # output: ['42', 'b']

```
### Linked List
> Linked lists can also be used to create other data structures, such as stack, queues and graphs.

A linked list is a sequence of nodes where each node stores its own data and a link to the next node.

Applications: Linked lists are useful when your data is linked. For example when you need undo/redo functionality, the nodes can represent the state with links to the previous and next states. Another example would be a playlist of music, where each clip is linked with the next one.


```python
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_front(self, data):
        self.head = Node(data, self.head)      

    def add_at_end(self, data):
        if not self.head:
            self.head = Node(data, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)

    def get_last_node(self):
        n = self.head
        while(n.next != None):
            n = n.next
        return n.data

    def is_empty(self):
        return self.head == None

    def print_list(self):
        n = self.head
        while n != None:
            print(n.data, end = " => ")
            n = n.next
        print()


s = LinkedList()
s.add_at_front(5)
s.add_at_end(8)
s.add_at_front(9)

s.print_list() # output: 9 => 5 => 8 =>
print(s.get_last_node())  # output: 8
```


### Graph

Graphs are used to represent many real-life applications like networks, transportation paths of a city, and social network connections.

A graph is a set of connected nodes where each node is called a Vertex and the connection between two of them is called an Edge.


```python
class Graph():
    def __init__(self, size):
        self.adj = [ [0] * size for i in range(size)]
        self.size = size

    def add_edge(self, orig, dest):
        if orig > self.size or dest > self.size or orig < 0 or dest < 0:
            print("Invalid Edge")
        else:
            self.adj[orig-1][dest-1] = 1
            self.adj[dest-1][orig-1] = 1

    def remove_edge(self, orig, dest):
        if orig > self.size or dest > self.size or orig < 0 or dest < 0:
            print("Invalid Edge")
        else:
            self.adj[orig-1][dest-1] = 0
            self.adj[dest-1][orig-1] = 0

    def display(self):
        for row in self.adj:
            print()
            for val in row:
                print('{:4}'.format(val),end="")

#a sample Graph
G = Graph(4)
G.add_edge(1, 3)
G.add_edge(3, 4)
G.add_edge(2, 4)
G.display()
# output:
# 0   0   1   0
# 0   0   0   1
# 1   0   0   1
# 0   1   1   0
```
