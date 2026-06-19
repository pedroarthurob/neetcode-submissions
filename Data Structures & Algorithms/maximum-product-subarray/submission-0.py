class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        min_prod = nums[0]
        max_prod = nums[0]
        answer = nums[0]

        for i in range(1, n):
            products = (
                nums[i],
                nums[i] * min_prod,
                nums[i] * max_prod            
            )

            max_prod = max(products)
            min_prod = min(products)

            answer = max(answer, max_prod)

        return answer