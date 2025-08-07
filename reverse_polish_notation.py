class Solution:
    
    def __init__(self, *args, **kwargs):
        self.stack = []
        self.operators = ("+", "-", "*", "/")
        super().__init__(*args, **kwargs)
    
    def evaluate(self, operator_1, operator_2, operator):
        if operator == "+":
            return operator_1 + operator_2
        elif operator == "-":
            return operator_1 - operator_2
        elif operator == "*":
            return operator_1 * operator_2
        elif operator == "/":
            return int(operator_1/operator_2)

    
    def evalRPN(self, tokens):
        for token in tokens:
            if token not in self.operators:
                self.stack.append(token)
            else:
                operator_2 = int(self.stack.pop())
                operator_1 = int(self.stack.pop())
                result = self.evaluate(operator_1, operator_2, token)
                self.stack.append(result)

        return int(self.stack[0])
