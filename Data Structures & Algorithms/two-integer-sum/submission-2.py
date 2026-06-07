class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for j in range(len(nums)):
            current_complement = target-nums[j]
            if current_complement in complements:
                return [complements[current_complement], j]

            else:
                complements[nums[j]] = j