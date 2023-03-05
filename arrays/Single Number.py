#this solution uses bit manipulation to give a result in O(n) in speed and O(1) in memory, beats 85% of solutions in speed and 86% of solutions in memory
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for i in nums:
            result^=i
        return(result)
