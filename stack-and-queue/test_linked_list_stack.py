from linked_list_stack import LinkedListStack


def main():
    print("Creating a stack...")
    a = LinkedListStack()
    print("Length of the stack:", len(a))
    print("The stack is empty:", a.is_empty())
    print()

    print("Pushing 10 to the stack...")
    a.push(10)
    print("The element at the top of the stack is", a.top())
    print("Length of the stack:", len(a))
    print("The stack is empty:", a.is_empty())
    print()

    print("Pushing 20 30 40 50 to the stack in this order...")
    a.push(20)
    a.push(30)
    a.push(40)
    a.push(50)
    print("The element at the top of the stack is", a.top())
    print("Length of the stack:", len(a))
    print("The stack is empty:", a.is_empty())
    print()

    print("Popping the stack...")
    a.pop()
    print("The element at the top of the stack is", a.top())
    print("Length of the stack:", len(a))
    print("The stack is empty:", a.is_empty())
    print()

    print("Popping the stack 4 times...")
    for i in range(3):
        a.pop()
    print("The element at the top of the stack is", a.top())
    print("Length of the stack:", len(a))
    print("The stack is empty:", a.is_empty())
    print()


if __name__ == "__main__":
    main()
