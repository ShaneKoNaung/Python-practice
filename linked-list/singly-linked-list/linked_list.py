from node import Node


class LinkedList(object):
    def __init__(self):
        ''' create an empty list '''
        self._head = None  # reference to the head Node
        self._tail = None  # reference to the tail Node
        self._size = 0     # number of elements in the list

    def __len__(self):
        ''' return the size of the list '''
        return self._size

    def is_empty(self):
        ''' return True if the list is empty '''
        return self._size == 0

    def push_front(self, data):
        ''' add to the front '''
        node = Node(data)              # create a new Node
        node.set_next(self._head)      # node.next = head
        self._size += 1                # increase size by one
        self._head = node              # head = Node
        if self._tail is None:          # if tail is none
            self._tail = node           # tail = Node

    def __str__(self):
        current = self._head
        output = ""
        while current:
            output += str(current) + "->"
            current = current.get_next()
        return output

    def top_front(self):
        ''' return front item '''
        return self._head.get_data()

    def pop_front(self):
        '''
        remove from front
        raise IndexError if the list is empty
        '''
        if self.is_empty():
            raise IndexError("List is empty")
        self._head = self._head.get_next()
        self._size -= 1
        if self._head is None:
            self._tail = None

    def push_back(self, data):
        '''
        add to end
        add at the front if the list is empty
        '''
        node = Node(data)
        if self._tail is None:
            self._tail = node
            self._head = self._tail
        else:
            self._tail.set_next(node)
            self._tail = node
        self._size += 1

    def top_back(self):
        ''' return back item '''
        if self._tail is None:
            raise IndexError("list is empty")
        else:
            return self._tail.get_data()

    def pop_back(self):
        ''' remove the last element '''
        if self._head is None:
            raise IndexError("List is empty")
        if self._head == self._tail:
            self._tail = None
            self._head = self._tail
        else:
            current = self._head
            while current.get_next().get_next() is not None:
                current = current.get_next()
            current.set_next(None)
            self._tail = current
        self._size -= 1

    def find(self, data):
        ''' return true if data is in the list '''
        if self.is_empty():
            raise IndexError("list is empty")
        else:
            current = self._head
            while current.get_data() != data:
                current = current.get_next()
                if current is None:
                    return False
            return True

    def delete(self, data):
        ''' delete the node containing the data '''
        if self.is_empty():
            raise IndexError("list is empty")
        if not self.find(data):
            raise IndexError("data is not in the list")
        else:
            current = self._head
            if current.get_data() == data:
                self.pop_front()
            elif self._tail.get_data() == data:
                self.pop_back()
            else:
                while current.get_next().get_data() != data:
                    current = current.get_next()
                current.set_next(current.get_next().get_next())
                self._size -= 1
