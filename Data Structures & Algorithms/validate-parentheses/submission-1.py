class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        opens = ['(', '{', '['] 
        closes = [')', "}", ']']
        
        for character in s:
            if len(myStack) == 0:
                if character in opens:
                    myStack.append(character)
                else:
                    return False

            else:
                top = myStack[-1]                
                if character == closes[opens.index(top)]:
                    myStack.pop()
                
                elif top in opens and character in opens:
                    myStack.append(character)

                else:
                    return False
                
        return len(myStack) == 0