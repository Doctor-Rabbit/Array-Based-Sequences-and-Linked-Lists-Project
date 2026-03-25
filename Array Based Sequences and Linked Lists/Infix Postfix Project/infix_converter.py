from stack import Stack


class InfixToPostfixConverter:
    """Converts infix expressions to postfix using a Stack."""

    PRECEDENCE = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
    }

    OPERATORS = set(PRECEDENCE.keys())

    def convert(self, expression):
        output = []
        operators = Stack()
        tokens = expression.split()

        for token in tokens:
            if self._is_operand(token):
                output.append(token)
            elif token == "(":
                operators.push(token)
            elif token == ")":
                while not operators.is_empty() and operators.peek() != "(":
                    output.append(operators.pop())

                if operators.is_empty():
                    raise ValueError("Mismatched parentheses")

                operators.pop()  # Remove '('
            elif token in self.OPERATORS:
                while (
                    not operators.is_empty()
                    and operators.peek() != "("
                    and self.PRECEDENCE[operators.peek()] >= self.PRECEDENCE[token]
                ):
                    output.append(operators.pop())

                operators.push(token)
            else:
                raise ValueError(f"Unsupported token: {token}")

        while not operators.is_empty():
            top = operators.pop()
            if top in {"(", ")"}:
                raise ValueError("Mismatched parentheses")
            output.append(top)

        return " ".join(output)

    def _is_operand(self, token):
        return token not in self.OPERATORS and token not in {"(", ")"}
