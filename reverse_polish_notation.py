class Solution:
    
    def __init__(self, *args, **kwargs):
        self.stack = []
        self.operators = ["+", "-", "*", "/"]
        self.operator_function_mapper = {
            "+": self._add,
            "-": self._subtract,
            "*": self._mul,
            "/": self._div
        }
        super().__init__(*args, **kwargs)

    
    def _add(self, operator_1, operator_2):
        return operator_1 + operator_2
    
    def _subtract(self, operator_1, operator_2):
        return operator_1 - operator_2
    
    def _mul(self, operator_1, operator_2):
        return operator_1 * operator_2
    
    def _div(self, operator_1, operator_2):
        return operator_1 / operator_2 # Truncates towards zero (floor but also with negative numbers). // will move -3.5 to 4 instead of 3
    
    def evalRPN(self, tokens):
        for token in tokens:
            if token not in self.operator_function_mapper:
                self.stack.append(token)
            else:
                operator_2 = int(self.stack.pop())
                operator_1 = int(self.stack.pop())
                result = self.operator_function_mapper.get(token)(operator_1, operator_2)
                self.stack.append(result)

        return int(self.stack[0])


