#this is  the implementation for the  Queue Data Structure
class DeQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        '''data structure  size  for the queue'''
        '''data structure  front  for the queue'''
        self._data = [None] * DeQueue.DEFAULT_CAPACITY 
        self._size = 0
        self._front = 0

    
    def __len__(self):
        '''return the number of elements in the queue'''
        return self._size
    
    def is_empty(self):
        '''returns true if the queue is empty'''
        return self._size == 0
    
    def first(self):
        '''Return {but  do not remove} the element at the front of the queue'''

        '''Raise an empty Exception if the queue is empty.'''
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._data[self._front]
    
    def last(self):
        '''Return {but  do not remove} the element at the back of the queue'''

        '''Raise an empty Exception if the queue is empty.'''
        if self.is_empty():
            raise Exception('Queue is empty')
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]
    
    def delete_first(self):
        '''Remove and return the  first element  from  the  queue using the FIFO structure'''
        '''Raise Empty Exception if the queue is empty'''
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front =  (self._front + 1) % len(self._data)
        self._size -= 1
        return answer
    
    def delete_last(self):
        '''Remove and  return the last element from the queue using the FIFO structure'''
        '''Raise Empty Exception if the queue is empty'''
        if self.is_empty():
            raise Exception("Queue is empty")
        answer = self.data[(self._front + self._size)  - 1 % len(self._data)]
        self._data[(self._front + self._size)  - 1 % len(self._data)] = None
        self._size -= 1
        return answer

    def add_first(self, e):
        '''Add an element to the front of the queue'''
        if(self._size == len(self._data)):
            self._resize(2 * len(self._data))
        back = ((self._front + self._size - 1) % len(self._data)) 
        while back >= self._front:
            self._data[back + 1] = self._data[back]
            back = back - 1
            print(self._data)
        self._size += 1
        self._data[self._front] = e
        
    
    def add_last(self, e):
        '''Add an element at the back of  the queue'''
        if(self._size == len(self._data)):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        '''Resize to a new list of capacity >= len(self)'''
        old = self._data #keep trtack of existing list
        self._data = [None] * cap #allocate list with new capacity
        walk = self._front
        for k  in range(self._size): #only consider existing elements
            self._data[k] = old[walk] #intentionally shift indices
            walk = (1+ walk) % len(old) #use old size as modulus
        self.front = 0 #front has been realigned

    def showElements(self):
        print(self._data)