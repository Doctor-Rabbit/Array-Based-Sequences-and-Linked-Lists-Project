from stack import Stack


class PostfixEvaluator:
    """Evaluates postfix expressions using a stack."""

    OPERATORS = {"+", "-", "*", "/"}

    def evaluate(self, expression):
        if not expression or not expression.strip():
            raise ValueError("Expression cannot be empty.")

        stack = Stack()
        tokens = expression.split()

        for token in tokens:
            if self._is_number(token):
                stack.push(float(token) if "." in token else int(token))
            elif token in self.OPERATORS:
                if stack.size() < 2:
                    raise ValueError(f"Invalid postfix expression: {expression}")

                right = stack.pop()
                left = stack.pop()
                result = self._apply_operator(left, right, token)
                stack.push(result)
            else:
                raise ValueError(f"Invalid token in postfix expression: {token}")

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
