'''
from Deque import DeQueue as  D

D1 = D()

D1.add_last(1)
D1.add_last(2)
D1.add_last(3)
D1.add_last(4)
D1.add_last(5)
D1.add_last(6)

D1.showElements()

D1.add_first(7)

print(D1.first())
D1.showElements()
D1.add_first(8)
D1.add_last(9)
D1.add_last(10)
D1.add_last(11)
print(D1.first())
print(D1.last())
D1.showElements()
'''
from Queue import Queue as Q
Q1 = Q()
for x in range (1, 20):
    Q1.enqueue(x)

print(Q1.first())

print(Q1.first())
for x in range(1, 4):
    Q1.dequeue()
print(Q1.first())
print(Q1.first())
Q1.enqueue(10)
Q1.enqueue(100)
while not Q1.is_empty():
    print(Q1.dequeue())
Q1.showElements()
