from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = Counter(nums)
        
        print(freq)

        buckets = [[] for _ in range(n + 1)]
        for num in freq:
            buckets[freq[num]].append(num)

        print(buckets)
        answer = []
        i = n - 1
        while k:
            if len(buckets[i]) > 0:
                for num in buckets[i]:
                    answer.append(num)
                k -= len(buckets[i])

            i -= 1
        
        return answer



        
