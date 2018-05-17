from linked_list import LinkedList
from node import Node
# from node import Node


def main():
    ll = LinkedList()

    print("List is empty :", ll.is_empty())
    print()

    print("adding 10 to the front")
    ll.push_front(10)

    print("adding 20 to the front")
    ll.push_front(20)

    print("The front item is:", ll.top_front())
    print("length now :", len(ll))
    print()

    print("Removing the first item ")
    ll.pop_front()
    print("The front item now is", ll.top_front())
    print()

    print("adding 30 at the end")
    ll.push_back(30)
    print("adding 40 at the end")
    ll.push_back(40)
    print("The last item is", ll.top_back())
    print("The length now is", len(ll))
    print()

    print("removing the last item...")
    ll.pop_back()
    print("The last item now is", ll.top_back())
    print("The length now is", len(ll))
    print()

    print("20 is in the list:", ll.find(20))
    print("10 is in the list:", ll.find(10))
    print()

    print("front item is ", ll.top_front())
    ll.delete(10)
    print("delete 10")
    print("front item is ", ll.top_front())
    print("length is now:", len(ll))


if __name__ == "__main__":
    main()
