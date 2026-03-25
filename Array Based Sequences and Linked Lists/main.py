from postfix_evaluator import PostfixEvaluator
from infix_converter import InfixToPostfixConverter
from singly_linked_list import SinglyLinkedList
from split_evens_odds import SplitEvensOdds


def format_result(value):
    if isinstance(value, float):
        return str(value)
    return str(value)


def test_postfix_evaluator():
    postfix = [
        "5 3 +",
        "8 2 - 3 +",
        "5 3 8 * +",
        "6 2 / 3 +",
        "5 8 + 3 -",
        "5 3 + 8 *",
        "8 2 3 * + 6 -",
        "5 3 8 * + 2 /",
        "8 2 + 3 6 * -",
        "5 3 + 8 2 / -"
    ]

    evaluator = PostfixEvaluator()

    print("----- Postfix Evaluator -----")
    for expr in postfix:
        result = evaluator.evaluate(expr)
        print(f"[{expr}] = {format_result(result)}")
    print()


def test_infix_converter():
    infix = [
        "A + B",
        "A + B * C",
        "( A + B ) * C",
        "A * B + C / D",
        "( A + B ) * ( C - D )",
        "A + B * C - D / E",
        "A * ( B + C ) / D",
        "( A + B * C ) / ( D - E )",
        "A + ( B - C ) * D",
        "( A + B * ( C - D ) ) / E"
    ]

    converter = InfixToPostfixConverter()

    print("----- Infix to Postfix Converter -----")
    for expr in infix:
        converted = converter.convert(expr)
        print(f"[{expr}] -> [{converted}]")
    print()


def test_singly_linked_list():
    print("---- Build a forward list ----")
    forward_list = SinglyLinkedList()
    forward_list.build_list_forward([10, 20, 30, 40, 50])
    print(forward_list)

    forward_list.delete_first()
    print("Delete the first node:", forward_list)

    forward_list.delete_last()
    print("Delete the last node:", forward_list)

    forward_list.delete_value(30)
    print("Delete the interior node:", forward_list)
    print()

    print("---- Build a backward list ----")
    backward_list = SinglyLinkedList()
    backward_list.build_list_backward([10, 20, 30, 40, 50])
    print(backward_list)

    backward_list.delete_first()
    print("Delete the first node:", backward_list)

    backward_list.delete_last()
    print("Delete the last node:", backward_list)

    backward_list.delete_value(30)
    print("Delete the interior node:", backward_list)
    print()

    print("---- Non-recursive reverse print test----")
    reverse_list = SinglyLinkedList()
    reverse_list.build_list_forward([10, 20, 30, 40, 50])
    print("Insertion order:", reverse_list)
    print("Reverse order (recursive):", reverse_list.display_reverse_recursive())
    print("Reverse order (non-recursive):", reverse_list.display_reverse_nr())
    print()

    print("---- Remove all test ----")
    remove_list = SinglyLinkedList()
    remove_list.build_list_forward([1, 2, 4, 6, 1, 3, 6])
    print(remove_list)

    remove_list.remove_all(1)
    print("Removing 1 and all duplicates:", remove_list)

    remove_list.remove_all(6)
    print("Removing 6 and all duplicates:", remove_list)
    print()


def test_split_evens_odds():
    print("---- Split Evens and Odds ----")
    split_list = SplitEvensOdds()
    split_list.build_list_forward([1, 2, 3, 4, 5, 6, 7, 8, 15, 14, 13, 12, 11, 10, 9])

    print(split_list)
    evens, odds = split_list.split()
    print(evens)
    print(odds)
    print(split_list)
    print()


def main():
    test_postfix_evaluator()
    test_infix_converter()
    test_singly_linked_list()
    test_split_evens_odds()


if __name__ == "__main__":
    main()
