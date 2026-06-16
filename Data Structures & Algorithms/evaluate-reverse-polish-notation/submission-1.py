class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack = []
        operators = {'+', '-', '/', '*'}

        for token in tokens:
            print(myStack, token)
            if token not in operators:
                myStack.append(int(token))

            else:
                n2 = myStack.pop()
                n1 = myStack.pop()

                if token == '+':
                    result = n1 + n2

                elif token == '-':
                    result = n1 - n2

                elif token == '/':
                    result = int(n1 / n2)

                else:
                    result = n1 * n2

                myStack.append(result)
        
        return myStack[0]