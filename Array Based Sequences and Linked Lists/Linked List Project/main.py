from singly_linked_list import SinglyLinkedList
from split_evens_odds import SplitEvensOdds


def test_forward_list():
    print("---- Build a forward list ----")
    linked_list = SinglyLinkedList()
    linked_list.build_list_forward([10, 20, 30, 40, 50])
    linked_list.display()

    linked_list.delete_first()
    print("Delete the first node:", end=" ")
    linked_list.display()

    linked_list.delete_last()
    print("Delete the last node:", end=" ")
    linked_list.display()

    linked_list.delete_value(30)
    print("Delete the interior node:", end=" ")
    linked_list.display()
    print()


def test_backward_list():
    print("---- Build a backward list ----")
    linked_list = SinglyLinkedList()
    linked_list.build_list_backward([10, 20, 30, 40, 50])
    linked_list.display()

    linked_list.delete_first()
    print("Delete the first node:", end=" ")
    linked_list.display()

    linked_list.delete_last()
    print("Delete the last node:", end=" ")
    linked_list.display()

    linked_list.delete_value(30)
    print("Delete the interior node:", end=" ")
    linked_list.display()
    print()


def test_reverse_print():
    print("---- Non-recursive reverse print test ----")
    linked_list = SinglyLinkedList()
    linked_list.build_list_forward([10, 20, 30, 40, 50])

    print("Insertion order:", end=" ")
    linked_list.display()

    print("Reverse order (recursive):", end=" ")
    linked_list.display_reverse_recursive()

    print("Reverse order (non-recursive):", end=" ")
    linked_list.display_reverse_nr()
    print()


def test_remove_all():
    print("---- Remove all test ----")
    linked_list = SinglyLinkedList()
    linked_list.build_list_forward([1, 2, 4, 6, 1, 3, 6])
    linked_list.display()

    linked_list.remove_all(1)
    print("Removing 1 and all duplicates:", end=" ")
    linked_list.display()

    linked_list.remove_all(6)
    print("Removing 6 and all duplicates:", end=" ")
    linked_list.display()
    print()


def test_split_evens_odds():
    print("---- Split evens and odds test ----")
    linked_list = SplitEvensOdds()
    linked_list.build_list_forward([1, 2, 3, 4, 5, 6, 7, 8, 15, 14, 13, 12, 11, 10, 9])

    print("Original list:", end=" ")
    linked_list.display()

    evens_list, odds_list = linked_list.split_evens_odds()

    print("Evens list:", end=" ")
    evens_list.display()

    print("Odds list:", end=" ")
    odds_list.display()

    print("Original list after split:", end=" ")
    linked_list.display()
    print()


def main():
    test_forward_list()
    test_backward_list()
    test_reverse_print()
    test_remove_all()
    test_split_evens_odds()


if __name__ == "__main__":
    main()
