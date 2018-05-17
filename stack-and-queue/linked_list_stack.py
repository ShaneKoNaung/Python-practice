''' implementation of stack using linked list '''


class LinkedListStack(object):
    class Node(object):
        def __init__(self, data, next=None):
            self._data = data
            self._next = next

    def __init__(self):
        ''' create  an empty stack '''
        self._head = None
        self._size = 0

    def __len__(self):
        ''' return the number of elements in the list'''
        return self._size

    def is_empty(self):
        ''' return True if the list is empty'''
        return self._size == 0

    def push(self, e):
        ''' add element at the top of the stack '''
        self._head = self.Node(e, self._head)
        self._size += 1

    def top(self):
        ''' return the element at the top of the stack'''
        if self.is_empty():
            raise IndexError("stack is empty")
        else:
            return self._head._data

    def pop(self):
        ''' remove and return the element at teh top of the stack'''
        if self.is_empty():
            raise IndexError("stack is empty")
        answer = self._head._data
        self._head = self._head._next
        self._size -= 1
        return answer
