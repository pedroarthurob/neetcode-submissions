class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        k = r
        while l <= r:
            candidate = (l + r) // 2
            time = 0
            for bananas in piles:
                time += bananas // candidate + int(bananas % candidate != 0)
            
            if time <= h:
                r = candidate - 1
                k = min(candidate, k)

            else:
                l = candidate + 1 

        return k
