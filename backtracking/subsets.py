#beats 58% in speed and 98% in memory
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def recur_subset(l):
            if len(l)==1:
                return([[],l])
            else:
                a=l[0]
                ch=l[1:]
                return(recur_subset(ch)+[sublist + [a] for sublist in recur_subset(ch)])
        return (recur_subset(nums))
