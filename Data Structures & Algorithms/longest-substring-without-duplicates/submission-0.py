class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        last_seen = {}

        l = 0 
        r = 0
        while l < len(s) and r < len(s):
            new_character = s[r]
            if new_character in last_seen:
                if l <= last_seen[new_character] and last_seen[new_character] <= r:
                    l = last_seen[new_character] + 1
                    
            last_seen[new_character] = r
            longest = max(longest, r - l + 1)
            r += 1

        return longest
