from singly_linked_list import SinglyLinkedList


class SplitEvensOdds(SinglyLinkedList):
    """
    Splits the current list into two separate lists by reassigning node pointers.
    No new data nodes are created during the split.
    """

    def split(self):
        evens = SinglyLinkedList()
        odds = SinglyLinkedList()

        evens_tail = None
        odds_tail = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = None

            if current.data % 2 == 0:
                if evens.head is None:
                    evens.head = current
                    evens_tail = current
                else:
                    evens_tail.next = current
                    evens_tail = current
            else:
                if odds.head is None:
                    odds.head = current
                    odds_tail = current
                else:
                    odds_tail.next = current
                    odds_tail = current

            current = next_node

        self.head = None
        return evens, odds
