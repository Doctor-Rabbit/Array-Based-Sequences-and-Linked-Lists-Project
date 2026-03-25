from stack import Stack


class InfixToPostfixConverter:
    """Converts infix expressions to postfix using a stack."""

    PRECEDENCE = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2
    }

    def convert(self, expression):
        if not expression or not expression.strip():
            raise ValueError("Expression cannot be empty.")

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
                    raise ValueError("Mismatched parentheses in expression.")

                operators.pop()  # Remove '('

            elif token in self.PRECEDENCE:
                while (
                    not operators.is_empty()
                    and operators.peek() != "("
                    and self.PRECEDENCE[operators.peek()] >= self.PRECEDENCE[token]
                ):
                    output.append(operators.pop())

                operators.push(token)

            else:
                raise ValueError(f"Invalid token in infix expression: {token}")

        while not operators.is_empty():
            top = operators.pop()
            if top in ("(", ")"):
                raise ValueError("Mismatched parentheses in expression.")
            output.append(top)

        return " ".join(output)

    def _is_operand(self, token):
        return token.isalnum()
