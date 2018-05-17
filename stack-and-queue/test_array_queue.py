from array_queue import QueueArray


def main():
    print("Creating a new queue...")
    q = QueueArray()
    print("length of the queue:", len(q))
    print("The queue is empty:", q.is_empty())
    print()

    print("Adding 10 to the queue...")
    q.enqueue(10)
    print("The front element is", q.first())
    print("length of the queue:", len(q))
    print("The queue is empty:", q.is_empty())
    print()

    print("Adding 20 30 40 50 in this order...")
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    print("The front element is", q.first())
    print("length of the queue:", len(q))
    print("The queue is empty:", q.is_empty())
    print()

    print("Dequeue 3 times...")
    for i in range(3):
        q.dequeue()
    print("The front element is", q.first())
    print("length of the queue:", len(q))
    print("The queue is empty:", q.is_empty())
    print()

    print("Adding 10 elements...")
    for i in range(10):
        q.enqueue(i)
    print("The front element is", q.first())
    print("length of the queue:", len(q))
    print("The queue is empty:", q.is_empty())
    print()


if __name__ == "__main__":
    main()
