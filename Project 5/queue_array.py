
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0
        self.front = 0
        self.back = 0

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == 0:
            return True
        else:
            return False



    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
           MUST have O(1) performance'''
        if self.num_items == self.capacity:
            return True
        else:
            return False


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError
           MUST have O(1) performance'''
        if not self.is_full():
            self.items[self.back] = item
            self.num_items += 1
            self.back += 1

            if self.back >= self.capacity:
                self.back = 0

        else:
            raise IndexError



    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError
           MUST have O(1) performance'''
        if not self.is_empty():
            first_in_queue = self.items[self.front]
            self.items[self.front] = None
            self.num_items -= 1
            self.front += 1

            if self.front == self.capacity:
                self.front = 0

            return first_in_queue

        else:
            raise IndexError

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
           MUST have O(1) performance'''
        return self.num_items
