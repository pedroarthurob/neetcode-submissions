class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        
        for i in range(n):
            start = i 
            tank = 0
            while (start - i) + 1 != n + 1:
                index = start % n
                tank += gas[index]

                print(start, i, 'start, i')
                print(index, 'index')
                print(tank, 'tank')
                print(cost[index], 'cost')

                if tank < cost[index]:
                    break 

                tank -= cost[index]
                start += 1
            
            if (start - i) + 1 == n + 1:
                return i
        
        return -1

            