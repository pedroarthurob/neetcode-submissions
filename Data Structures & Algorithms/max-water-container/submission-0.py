class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calcArea(i, j):
            return min(heights[i], heights[j]) * (j - i)
        
        i = 0
        j = len(heights) - 1

        answer = -1
        while i < j:
            answer = max(answer, calcArea(i, j))
            if heights[i] < heights[j]:
                i = i + 1
            
            else:
                j = j - 1

        return answer