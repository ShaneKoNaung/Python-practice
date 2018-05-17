''' implementation of queue by using array(list in python) '''


class QueueArray(object):
    DEFAULT_CAPACITY = 10  # moderate capacity for the queue

    def __init__(self):
        ''' create an empty list of DEFAULT_CAPACITY '''
        self._data = [None] * QueueArray.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        ''' return the size of the queue '''
        return self._size

    def is_empty(self):
        ''' return True if the queue is empty '''
        return self._size == 0

    def first(self):
        ''' return the first element in the queue'''
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self._data[self._front]

    def dequeue(self):
        ''' remove and return the first element of the queue '''
        if self.is_empty():
            raise IndexError('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        ''' add an element at the end of the queue '''
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        avil = (self._front + self._size) % len(self._data)
        self._data[avil] = e
        self._size += 1

    def resize(self, cap):
        ''' resize to a new list of capacity '''
        old_list = self._data
        new_list = [None] * cap
        current = self._front
        for i in range(self._size):
            new_list[i] = old_list[current]
            current = (current + 1) % len(old_list)
        self._data = new_list
        self._front = 0
