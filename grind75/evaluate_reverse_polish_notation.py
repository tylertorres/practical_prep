from math import floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        eval_stack = []

        operator_eval = {
            "+": lambda x, y : x + y,
            "-": lambda x, y : x - y,
            "/": lambda x, y : int(x / y),
            "*": lambda x, y : x * y
        }

        for token in tokens:
            if token in operator_eval:
                second_operand = eval_stack.pop()
                first_operand = eval_stack.pop()
                eval_stack.append(operator_eval[token](int(first_operand), int(second_operand)))
            else:
                eval_stack.append(int(token))
            
        
        return eval_stack[0]
        
