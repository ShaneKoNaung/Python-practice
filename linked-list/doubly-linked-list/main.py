from linked_list import LinkedList


def main():
    print("initialize a LinkedList")
    ll = LinkedList()
    print()

    print("Is the list empty?", ll.is_empty())
    print("length of the list:", len(ll))
    print()

    print("add 1 to the front")
    ll.push_front(1)
    print("The first item is:", ll.top_front())
    print("add 2 to the front")
    ll.push_front(2)
    print("The first item is:", ll.top_front())
    print("add 3 to the front")
    ll.push_front(3)
    print("The first item is:", ll.top_front())
    print("The length of the list is:", len(ll))
    print()

    print("removing the first item...")
    ll.pop_front()
    print("The first item is:", ll.top_front())
    print("The length of the list is:", len(ll))
    print("removing the first item...")
    ll.pop_front()
    print("The first item is:", ll.top_front())
    print("The length of the list is:", len(ll))
    print("removing the first item...")
    ll.pop_front()
    print("The length of the list is:", len(ll))
    print()


    print("adding the last item...")
    ll.push_back(1)
    print("The last item is:", ll.top_back())
    print("The length of the list is:", len(ll))
    print("adding the last item...")
    ll.push_back(2)
    print("The last item is:", ll.top_back())
    print("The length of the list is:", len(ll))
    print("adding the last item...")
    ll.push_back(3)
    print("The last item is:", ll.top_back())
    print("The length of the list is:", len(ll))
    print()

    print("3 is in the list", ll.find(3))
    print("10 is in the list", ll.find(10))
    print()

    print("removing 1 from the list")
    ll.delete(1)
    print("The length of the list is", len(ll))
    print("removing 3 from the list")
    ll.delete(3)
    print("The length of the list is", len(ll))


if __name__ == "__main__":
    main()
