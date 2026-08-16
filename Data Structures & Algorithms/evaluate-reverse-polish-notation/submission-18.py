import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.s = []

        for t in tokens:
            if t in "+-*/":
                right_var = self.s.pop()
                left_val = self.s.pop()
                if t == "+":
                    val = left_val + right_var
                elif t == '-':
                    val = left_val - right_var
                elif t == '*':
                    val = left_val * right_var
                else:
                    val = int(left_val/right_var)
            else:
                val = int(t)
            
            self.s.append(val)

        return self.s.pop()