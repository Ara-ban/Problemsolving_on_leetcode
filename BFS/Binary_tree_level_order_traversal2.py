#beats 75.3% in speed, 89.1% in memory
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return([])
        a=[root,0]
        q=deque([a])
      #deque usage as a queue
        result= deque()
      #deque usage as the order is requested to be from left to right
        i=0
        l=[]
        while q :
            a=q.popleft()
            if a[0] is not None:
                if (a[1]>i):
                    result.appendleft(l)
                    l=[]
                    i+=1
                l.append(a[0].val) 
                q.append([a[0].left,a[1]+1]) 
                q.append([a[0].right,a[1]+1])              
        result.appendleft(l)
        return(result)
