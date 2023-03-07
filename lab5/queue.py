class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

        self.display_queue()

    def pop(self):
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

    def display_queue(self):
        print("BACK", end=" ")

        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next

        print("FRONT")

    def is_empty(self):
        if self.head is None:
            print("THE QUEUE IS EMPTY")
        else:
            print("THE QUEUE IS NOT EMPTY")


def main():
    queue = Queue()

    print(
        "Menu Options:\n"
        "\t1. Display Queue\n"
        "\t2. Push\n"
        "\t3. Pop\n"
        "\t4. Check If The Queue Is Empty"
    )

    cont = "y"
    while cont.lower() == "y":
        op = int(input("\nEnter option: "))

        if op == 1:
            queue.display_queue()
        elif op == 2:
            new = int(input("Enter number to push: "))
            queue.push(new)
        elif op == 3:
            queue.pop()
        elif op == 4:
            queue.is_empty()

        cont = input("Continue? (Y/N): ")


main()
