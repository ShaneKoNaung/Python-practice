''' implementing queue using linked-list'''


class LinkedListQueue(object):
    class Node(object):
        def __init__(self, data, next=None):
            self._data = data
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        ''' return the number of element in the queue'''
        return self._size

    def is_empty(self):
        ''' return True if the queue is emtpy'''
        return self._size == 0

    def first(self):
        ''' return the first element in the queue '''
        return self._head._data

    def dequeue(self):
        ''' remove the first element in the queue '''
        if self.is_empty():
            raise IndexError("queue is empty")
        answer = self._head._data
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        ''' add an element at the end of the queue'''
        node = self.Node(e)
        if self.is_empty():
            self._head = node
        else:
            self._tail._next = node
        self._tail = node
        self._size += 1
