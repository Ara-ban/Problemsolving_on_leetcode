#beats 95% of solutions
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=n*(n+1)//2
        for i in nums:
            total-=i
        return (total)
