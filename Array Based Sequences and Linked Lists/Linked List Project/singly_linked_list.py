class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def build_list_forward(self, values):
        for value in values:
            self.insert_at_tail(value)

    def build_list_backward(self, values):
        for value in values:
            self.insert_at_head(value)

    def delete_first(self):
        if self.head is not None:
            self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def delete_value(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None and current.next.data != value:
            current = current.next

        if current.next is not None:
            current.next = current.next.next

    def remove_all(self, value):
        while self.head is not None and self.head.data == value:
            self.head = self.head.next

        current = self.head
        while current is not None and current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
            else:
                current = current.next

    def display(self):
        current = self.head
        result = "Head -> "

        while current is not None:
            result += f"{current.data} -> "
            current = current.next

        result += "None"
        print(result)

    def display_reverse_recursive(self):
        print("None <- ", end="")
        self._display_reverse_recursive_helper(self.head)
        print("Head")

    def _display_reverse_recursive_helper(self, node):
        if node is None:
            return
        self._display_reverse_recursive_helper(node.next)
        print(f"{node.data} <- ", end="")

    def display_reverse_nr(self):
        stack = []
        current = self.head

        while current is not None:
            stack.append(current.data)
            current = current.next

        print("None <- ", end="")
        while stack:
            value = stack.pop()
            if stack:
                print(f"{value} <- ", end="")
            else:
                print(f"{value} <- ", end="")
        print("Head")
