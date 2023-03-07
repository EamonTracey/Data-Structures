class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

        self.display_stack()

    def pop(self):
        if self.head is not None:
            self.head = self.head.next

        self.display_stack()

    def display_top(self):
        if self.head is None:
            print("THE STACK IS EMPTY")
        else:
            print("TOP OF STACK:", self.head.data)

    def display_stack(self):
        print("TOP", end=" ")

        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next

        print("BOTTOM")

    def is_empty(self):
        if self.head is None:
            print("THE STACK IS EMPTY")
        else:
            print("THE STACK IS NOT EMPTY")


def main():
    stack = Stack()

    print(
        "Menu Options:\n"
        "\t1. Display Stack\n"
        "\t2. Push\n"
        "\t3. Pop\n"
        "\t4. Check If The Stack Is Empty\n"
        "\t5. Display Top of Stack"
    )

    cont = "y"
    while cont.lower() == "y":
        op = int(input("\nEnter option: "))

        if op == 1:
            stack.display_stack()
        elif op == 2:
            new = int(input("Enter number to push: "))
            stack.push(new)
        elif op == 3:
            stack.pop()
        elif op == 4:
            stack.is_empty()
        elif op == 5:
            stack.display_top()

        cont = input("Continue? (Y/N): ")


main()
