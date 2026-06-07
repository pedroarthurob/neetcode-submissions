class Solution:
    def isPalindrome(self, s: str) -> bool:
        candidate = ""
        for character in s:
            if character.isdigit() or character.isalpha():
                candidate += character.lower()
        
        i = 0
        j = len(candidate)-1

        while i <= j:
            if candidate[i] != candidate[j]:
                return False
            
            i += 1
            j -= 1

        return True    