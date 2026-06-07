class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_array = [c for c in s]
        t_array = [c for c in t]
        s_array.sort()
        t_array.sort()

        for i in range(len(s)):
            if s_array[i] != t_array[i]:
                return False

        return True
        