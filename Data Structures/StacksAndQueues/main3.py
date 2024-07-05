from Deque2 import Deque as D

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