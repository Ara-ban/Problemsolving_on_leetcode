#this solution uses a set that keeps track of its elements via hashing, the solution is O(n) in complexity with it being better overall than the sort method
#or converting then cheking the difference of length method in number of operations 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        non_dup={nums[0]}
        for i in nums[1:]:
            if i in non_dup:
                return(True)
            non_dup.add(i)
        return False
        
