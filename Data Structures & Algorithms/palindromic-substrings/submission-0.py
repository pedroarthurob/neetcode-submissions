class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def expand(l, r):
            count = 0
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            return count

        answer = 0
        for i in range(n):
            answer += expand(i, i) + expand(i, i+1)
        
        return answer