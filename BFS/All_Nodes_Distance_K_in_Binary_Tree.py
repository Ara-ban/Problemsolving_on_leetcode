# Beats 80% in speed

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return([])
        parent ={}
        q=deque([root])
        while q:
            a = q.popleft()
            if a.left is not None:
                parent[a.left.val]=a
                q.append(a.left)
            if a.right is not None:
                parent[a.right.val]=a
                q.append(a.right)
        visited={}
        ans=[]
        q.append(target)
        while k>0 and q:
            size=len(q)
            while size:
                a=q.popleft()
                print(a.val)
                visited[a.val]=1
                if a.val in parent and parent[a.val].val not in visited:
                    q.append(parent[a.val])
                if a.left is not None and a.left.val not in visited:
                    q.append(a.left)
                if a.right is not None and a.right.val not in visited:
                    q.append(a.right)
                size-=1
            k-=1

        for a in q:
            ans.append(a.val)
        return(ans)
