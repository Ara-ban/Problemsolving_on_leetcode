from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        couples = [(frequency, element) for element, frequency in count.items()]

        couples.sort(reverse=True, key=lambda x: x[0])
        
        output = [element for _, element in couples[:k]]
        
        return output