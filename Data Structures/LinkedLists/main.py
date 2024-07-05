from LinkedStack import LinkedStack as Stack
from LinkedQueue import LinkedQueue as Queue
from CircularQueue import CircularQueue as CircularQueue
from LinkedDeque import LinkedDeque as Deque
from PositionalList import PositionalList as PositionalList
Q = Queue()
S = Stack()
CircQ = CircularQueue()
D = Deque()
P = PositionalList()
'''
#Adding elements to the stack
S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.push(5)

#Removing elements from the stack
print(S.pop())
print(S.pop())
print(S.pop())
print(S.pop())
print(S.pop())
print(S.pop())

#Adding elements to the Queue
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)

#Removing elements from the Queue
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
'''
'''
#adding elements to the Circular Queue
CircQ.enqueue(1)
CircQ.enqueue(2)
CircQ.enqueue(3)
#printing elements from the Circular Queue
CircQ.rotate()
print(CircQ.dequeue())
print(CircQ.dequeue())
print(CircQ.dequeue())
'''
'''
#adding elements to the Deque
D.insert_first(1)
D.insert_first(2)
D.insert_first(3)
#removing elements from the Deque
print(D.delete_last())
print(D.delete_last())
print(D.delete_last())
print(D.delete_last())
'''

#adding elements to the PositionalList
P.add_first(1)
P.add_first(2)
P.add_first(3)
P.add_first(4)
P.add_first(5)
P.add_first(6)
P.add_last(7)
#Print the elements from the PositionalList
for x in P:
    print(x)
print("Delete the last element from the list")
P.delete(P.last())
#Print the elements from the PositionalList
for x in P:
    print(x)