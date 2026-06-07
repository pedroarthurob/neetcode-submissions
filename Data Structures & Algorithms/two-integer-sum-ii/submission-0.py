class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        # found = False
        # while not found:
        #     ...
        while  l < r:
            current_sum = numbers[l] + numbers[r]
            if current_sum == target:
                return [l+1, r+1]
            
            elif current_sum > target:
                r = r - 1
            
            else:
                l = l + 1

        
