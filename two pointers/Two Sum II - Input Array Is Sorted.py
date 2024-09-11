from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j=0,len(numbers)-1
        a = numbers[i]+numbers[j]
        while a !=target : 
            if a> target:
                j-=1
            else: 
                i+=1
            a = numbers[i]+numbers[j]
        return[i+1,j+1]