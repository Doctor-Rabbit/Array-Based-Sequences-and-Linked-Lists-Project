from singly_linked_list import SinglyLinkedList


class SplitEvensOdds(SinglyLinkedList):
    def split_evens_odds(self):
        evens_list = SinglyLinkedList()
        odds_list = SinglyLinkedList()

        even_tail = None
        odd_tail = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = None

            if current.data % 2 == 0:
                if evens_list.head is None:
                    evens_list.head = current
                    even_tail = current
                else:
                    even_tail.next = current
                    even_tail = current
            else:
                if odds_list.head is None:
                    odds_list.head = current
                    odd_tail = current
                else:
                    odd_tail.next = current
                    odd_tail = current

            current = next_node

        self.head = None
        return evens_list, odds_list
