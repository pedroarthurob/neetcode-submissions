class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        pairs = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for character in s:
            if character in pairs:
                myStack.append(character)

            else:
                if len(myStack) == 0 or pairs[myStack.pop()] != character:
                    return False  
                
        return not myStack