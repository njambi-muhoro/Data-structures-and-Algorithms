# stacks - last in first out principle
#creating an empty list
letters = []

#adding elements to the stack
letters.append('a')
letters.append('b')
letters.append('c')
letters.append('d')
print(letters)

#removing elements from the stack - removes the last element in the stack
letters.pop()
print(letters)

#creating an empty queue
fruits = []

#adding elements into the queue - follows the first in first out principle
fruits.append('mango')
fruits.append('pineapple')
fruits.append('orange')
print(fruits)

# removing an element from the queue - removes element from the from using pop and indexing
fruits.pop(0)
fruits.pop(1)
print(fruits)

                                                 # DEQUEUE LIBRARY
from collections import deque
# ccreating a stack using deque  pushes or adds at the end
numbers = deque()
numbers.append(1)
numbers.append(2)
numbers.append(3)
print(numbers)
print(numbers)
#removing an element from the stack using deque removes from the end
numbers.pop()
print(numbers)

#creating a queue using deque 
letters = deque()

#adding elements into the queue using deque pushes or adds at the end
letters.append('q')
letters.append('r')
letters.append('s')
letters.append('t')
print(letters)

#removing elements from the queue using deque - removes from the front
letters.popleft()
letters.popleft()
print(letters)