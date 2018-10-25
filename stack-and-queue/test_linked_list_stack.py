from linked_list_stack import LinkedListStack
import pytest


a = LinkedListStack()
b = LinkedListStack()
c = LinkedListStack()
d = LinkedListStack()

a_element = [1,2,3,4,5]
b_element = ['a','b','c']
c_element = [2,4,1,3,5]

for i in a_element:
    a.push(i)
for i in b_element:
    b.push(i)
for i in c_element:
    c.push(i)

def test_len():
    assert len(a) == 5
    assert len(b) == 3
    assert len(c) == 5
    assert len(d) == 0

def test_is_empty():
    assert a.is_empty() == False
    assert b.is_empty() == False
    assert d.is_empty() == True

def test_top():
    assert a.top() == 5
    assert b.top() == 'c'
    assert c.top() == 5
    with pytest.raises(IndexError):
        d.top()

def test_pop():
    for i in reversed(a_element):
        assert a.pop() == i
    for i in reversed(b_element):
        assert b.pop() == i
    for i in reversed(c_element):
        assert c.pop() == i
    with pytest.raises(IndexError):
        d.pop()
