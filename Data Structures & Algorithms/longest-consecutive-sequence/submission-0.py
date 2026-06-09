class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starters = set(nums)

        longest = 0
        for num in starters:
            if num-1 not in starters:
                
                i = num
                length = 0
                while i in starters:
                    length += 1
                    i += 1

                longest = max(length, longest)
        
        return longest                