class ArrayStack(object):
    ''' implementation of stack using array(list in python)'''
    def __init__(self):
        ''' create a empty list '''
        self._data = []

    def __len__(self):
        ''' returns the number of elements in the stack '''
        return len(self._data)

    def is_empty(self):
        ''' returns True if the list is empty '''
        return len(self._data) == 0

    def push(self, e):
        ''' add element to the top of the stack '''
        self._data.append(e)

    def top(self):
        ''' return the element at the top of the stack '''
        if self.is_empty():
            raise IndexError("stack is empty")
        else:
            return self._data[-1]

    def pop(self):
        ''' returns and removes element at the top of the stack '''
        if self.is_empty():
            raise IndexError("stack is empty")
        else:
            return self._data.pop()
