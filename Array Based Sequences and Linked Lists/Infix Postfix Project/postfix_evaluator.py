from stack import Stack


class PostfixEvaluator:
    """Evaluates postfix expressions using a Stack."""

    OPERATORS = {"+", "-", "*", "/"}

    def evaluate(self, expression):
        stack = Stack()
        tokens = expression.split()

        for token in tokens:
            if self._is_number(token):
                stack.push(self._to_number(token))
            elif token in self.OPERATORS:
                if stack.size() < 2:
                    raise ValueError(f"Invalid postfix expression: {expression}")

                right = stack.pop()
                left = stack.pop()
                result = self._apply_operator(left, right, token)
                stack.push(result)
            else:
                raise ValueError(f"Unsupported token: {token}")

        if stack.size() != 1:
            raise ValueError(f"Invalid postfix expression: {expression}")

        return stack.pop()

    def _apply_operator(self, left, right, operator):
        if operator == "+":
            return left + right
        if operator == "-":
            return left - right
        if operator == "*":
            return left * right
        if operator == "/":
            return left / right
        raise ValueError(f"Unsupported operator: {operator}")

    def _is_number(self, token):
        try:
            float(token)
            return True
        except ValueError:
            return False

    def _to_number(self, token):
        value = float(token)
        return int(value) if value.is_integer() else value
