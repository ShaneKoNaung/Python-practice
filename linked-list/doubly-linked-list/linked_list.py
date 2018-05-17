from node import Node


class LinkedList(object):
    # initialize a head pointer and a tail pointer
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    # return true if the list is empty
    def is_empty(self):
        return self._size == 0

    # return the size of the list
    def __len__(self):
        return self._size

    # add an element at the front of the list
    def push_front(self, data):
        # create a Node
        node = Node(data)
        # if the list is empty
        if self.is_empty():
            # set head and tail pointers the Node
            self._head = node
            self._tail = self._head
        else:
            # set node's next to the _head
            node.set_next(self._head)
            # set front'prev to the Node
            self._head.set_prev(node)
            # set head pointer to the Node
            self._head = node
        # increase the size by one
        self._size += 1

    # return the first item
    def top_front(self):
        # if the list is empty, raise error
        if self.is_empty():
            raise IndexError("list is empty")
        else:
            return self._head.get_data()

    # remove the first item
    def pop_front(self):
        # if the list is empty, raise error
        if self.is_empty():
            raise IndexError("list is empty")
        else:
            front_node = self._head
            # set the head pointer to front_node's next
            self._head = front_node.get_next()
            # if the new front node is None
            if self._head is None:
                self._tail = self._head
            else:
                # set the head's prev to None
                self._head.set_prev(None)
            self._size -= 1

    # add an element at the end of the list
    def push_back(self, data):
        # create a Node
        node = Node(data)
        # list is empty
        if self.is_empty():
            self.push_front(data)
        else:
            last_node = self._tail
            last_node.set_next(node)
            node.set_prev(last_node)
            self._tail = node
            self._size += 1

    # return the last item
    def top_back(self):
        # list is empty
        if self.is_empty():
            raise IndexError('list is empty')
        else:
            return self._tail.get_data()

    # remove the last item
    def pop_back(self):
        # list is_empty
        if self.is_empty():
            raise IndexError("list is empty")
        else:
            last_node = self._tail
            if last_node.get_prev() is None:
                self.pop_front()
            else:
                # set the second last node's next to None
                last_node.get_prev().set_next(None)
                self._tail = last_node.get_prev()
                self._size -= 1

    # return true if the element is in the list
    def find(self, data):
        # list is_empty
        if self.is_empty():
            return False
        else:
            current = self._head
            if current.get_data() == data:
                return True
            if self._tail.get_data() == data:
                return True
            if self._head == self._tail:
                return False
            else:
                while current.get_data() != data:
                    current = current.get_next()
                    if current is None:
                        return False
                return True

    # delete an element
    def delete(self, data):
        # list is_empty
        if self.is_empty():
            raise IndexError('list is empty')
        elif not self.find(data):
            raise ValueError('element is not in the list')
        else:
            # if there is only one element in the list
            # or the element is first element
            if self._head == self._tail or self._head.get_data() == data:
                self.pop_front()
            # if the element is in the end
            elif self._tail.get_data() == data:
                self.pop_back()
            else:
                current = self._head
                while current != self._tail:
                    if current.get_data() == data:
                        current.get_prev().set_next(current.get_next())
                        current.get_next().set_prev(current.get_prev())
                self._size -= 1
