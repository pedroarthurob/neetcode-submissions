class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left = [0] * n
        right = [0] * n
        
        left_max = height[0]
        for i in range(n):
            left_max = max(left_max, height[i])
            left[i] = left_max

        right_max = height[-1]
        for i in range(n-1, -1, -1):
            right_max = max(right_max, height[i])
            right[i] = right_max

        answer = 0
        for i in range(n):
            answer += min(left[i], right[i]) - height[i]
        
        return answer
