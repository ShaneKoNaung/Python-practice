class Node(object):
    def __init__(self, data=None, next=None):
        ''' initialize the node '''
        self._data = data  # data
        self._next = next  # next pointer

    def get_data(self):
        ''' return data '''
        return self._data

    def set_data(self, data):
        ''' set the value of data '''
        self._data = data

    def get_next(self):
        ''' return next '''
        return self._next

    def set_next(self, next_Node):
        ''' set the value of data '''
        self._next = next_Node

    def __str__(self):
        return str(self._data)
