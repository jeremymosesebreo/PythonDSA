import collections
D = collections.deque()
class Deque:
    def __len__(self):
        return len(D)
    def add_first(self,e):
        D.appendleft(e)
    def add_last(self,e):
        D.append(e)
    def delete_first(self):
        return D.popleft()
    def delete_last(self):
        return D.pop()
    def first(self):
        return D[0]
    def last(self):
        return D[-1]
    def showElements(self):
        print(D)
    def clear(self):
        D.clear()