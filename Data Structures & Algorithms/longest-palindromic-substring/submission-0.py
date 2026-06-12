class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = s[0]
        n = len(s)
        def expand(l, r):
            current = ""
            while l >= 0 and r < n and s[l] == s[r]:
                currentLen = r - l + 1
                if currentLen > len(best):
                    print(f"here {l} {r} {s[l:r+1]}")
                    current = s[l:r + 1]
                l -= 1
                r += 1
            
            return current

        for i in range(n):
            best = max(
                best,
                expand(i, i),
                expand(i, i + 1), 
                key=len)

        return best            