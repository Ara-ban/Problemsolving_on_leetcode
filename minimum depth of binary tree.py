#this solution beats 98% in speed and 72% in memory 
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q=deque([root])
        if root:
            ans=1
        else:
            return(0)
        while q:
            for j in range(len(q)):
                node=q.popleft()
                if node:
                    if node.left==None and node.right==None:
                        return(ans)
                    else:
                        if node.left:
                            q.append(node.left)
                        if node.right:
                            q.append(node.right)
            ans+=1
        return(ans)
