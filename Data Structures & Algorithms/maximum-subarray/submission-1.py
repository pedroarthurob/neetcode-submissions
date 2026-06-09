class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        [2, 3, -9, 4, 5, 6 ,7]
        
        currSum = nums[0]

        answer = nums[0]
        for i in range(1, len(nums)):
            
            if currSum + nums[i] <= nums[i]:
                currSum = nums[i]
            
            else:
                currSum += nums[i]

            answer = max(answer, currSum)

        return answer

        