class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["*", "-", "+", "/"]
        stack = []
        for item in tokens:
            if item not in operators:
                stack.append(int(item))
            else:
                operand_1 = stack.pop()
                operand_2 = stack.pop()
                result=None
                match item:
                    case "+":
                        result = operand_1 + operand_2
                    case "*":
                        result = operand_1 * operand_2
                    case "-":
                        result = operand_2 - operand_1
                    case "/":
                        result = int(operand_2/operand_1)

                stack.append(result)
        
        return stack[0]
                
        
