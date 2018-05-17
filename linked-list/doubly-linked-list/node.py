class Node(object):
    # initialize a Node
    def __init__(self, data=None, next=None, prev=None):
        self._data = data
        self._next = next
        self._prev = prev

    # return _data
    def get_data(self):
        return self._data

    # set _data
    def set_data(self, data):
        self._data = data

    # return _next
    def get_next(self):
        return self._next

    # set _next
    def set_next(self, Node):
        self._next = Node

    # return _prev
    def get_prev(self):
        return self._prev

    # set _prev
    def set_prev(self, Node):
        self._prev = Node
        
    def __str__(self):
        return str(self.get_data())
