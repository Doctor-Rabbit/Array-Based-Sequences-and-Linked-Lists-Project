from stack import Stack


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

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def build_list_forward(self, values):
        self.head = None
        for value in values:
            self.append(value)

    def build_list_backward(self, values):
        self.head = None
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
            return False

        if self.head.data == value:
            self.head = self.head.next
            return True

        prev = self.head
        current = self.head.next

        while current is not None:
            if current.data == value:
                prev.next = current.next
                return True
            prev = current
            current = current.next

        return False

    def remove_all(self, value):
        while self.head is not None and self.head.data == value:
            self.head = self.head.next

        current = self.head
        prev = None

        while current is not None:
            if current.data == value:
                prev.next = current.next
            else:
                prev = current
            current = current.next

    def display_reverse_recursive(self):
        values = []
        self._collect_reverse_recursive(self.head, values)
        return "None <- " + " <- ".join(values) + " <- Head"

    def _collect_reverse_recursive(self, node, values):
        if node is None:
            return
        self._collect_reverse_recursive(node.next, values)
        values.append(str(node.data))

    def display_reverse_nr(self):
        stack = Stack()
        current = self.head

        while current is not None:
            stack.push(current.data)
            current = current.next

        parts = ["None"]
        first = True
        while not stack.is_empty():
            if first:
                parts.append(f"<- {stack.pop()}")
                first = False
            else:
                parts.append(f"-> {stack.pop()}")

        parts.append("<- Head")
        return " ".join(parts)

    def __str__(self):
        parts = ["Head"]
        current = self.head

        while current is not None:
            parts.append(f"-> {current.data}")
            current = current.next

        parts.append("-> None")
        return " ".join(parts)
