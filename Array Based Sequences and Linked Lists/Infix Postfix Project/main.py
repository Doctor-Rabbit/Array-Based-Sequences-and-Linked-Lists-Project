from postfix_evaluator import PostfixEvaluator
from infix_converter import InfixToPostfixConverter


def main():
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
        "5 3 + 8 2 / -",
    ]

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
        "( A + B * ( C - D ) ) / E",
    ]

    evaluator = PostfixEvaluator()
    converter = InfixToPostfixConverter()

    print("----- Postfix Evaluator -----")
    for expression in postfix:
        print(f"[{expression}] = {evaluator.evaluate(expression)}")

    print()
    print("----- Infix to Postfix Converter -----")
    for expression in infix:
        print(f"[{expression}] -> [{converter.convert(expression)}]")


if __name__ == "__main__":
    main()
