class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class Dequeue:
    def __init__(self):
        self.head = None

    def display_queue(self):
        print("BACK", end=" ")

        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next

        print("FRONT")

    def push_front(self, data):
        if self.head is None:
            self.push_back(data)
            return

        node = Node(data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node

        self.display_queue()

    def push_back(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

        self.display_queue()

    def pop_front(self):
        curr = self.head

        if curr is None:
            self.display_queue()
            return
        if curr.next is None:
            self.head = None
            self.display_queue()
            return

        while curr.next.next is not None:
            curr = curr.next
        curr.next = None

        self.display_queue()

    def pop_back(self):
        if self.head is not None:
            self.head = self.head.next

        self.display_queue()

    def is_empty(self):
        if self.head is None:
            print("THE QUEUE IS EMPTY")
        else:
            print("THE QUEUE IS NOT EMPTY")


def main():
    queue = Dequeue()

    print(
        "Menu Options:\n"
        "\t1. Display Queue\n"
        "\t2. Push Front\n"
        "\t3. Push Back\n"
        "\t4. Pop Front\n"
        "\t5. Pop Back\n"
        "\t6. Check If The Queue Is Empty"
    )

    cont = "y"
    while cont.lower() == "y":
        op = int(input("\nEnter option: "))

        if op == 1:
            queue.display_queue()
        elif op == 2:
            new = int(input("Enter number to push: "))
            queue.push_front(new)
        elif op == 3:
            new = int(input("Enter number to push: "))
            queue.push_back(new)
        elif op == 4:
            queue.pop_front()
        elif op == 5:
            queue.pop_back()
        elif op == 6:
            queue.is_empty()

        cont = input("Continue? (Y/N): ")


main()
