# this solution beats 97% in speed and 85% in memory, it should be mentionned that the treeNode datastructure that this problem works with can be implemented as follows:
#class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#       self.val = val
#       self.left = left
#       self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=deque([root])
        output=[]
        while q:
            sum=0
            i=0
            for j in range(len(q)):
                node=q.popleft()
                if node:
                    i+=1
                    sum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            output.append(sum/i)
        return(output)
