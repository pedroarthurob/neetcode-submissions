class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        answer = []
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -(nums[i])
            j = i + 1
            k = len(nums) - 1
            while j < k:
                current_sum = nums[j] + nums[k]
                if current_sum > target:
                    k = k -1
                elif current_sum < target:
                    j = j + 1

                else:
                    answer.append([nums[i], nums[j], nums[k]])
                    previous_j = nums[j]
                    previous_k = nums[k]
                    while j < k and nums[j] == previous_j:
                        j = j + 1

                    while j < k and nums[k] == previous_k:
                        k = k - 1
                    
        return answer
