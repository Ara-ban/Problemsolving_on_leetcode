#beats 82% in speed and and 57% on memory, simple solution using recursion.
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        #if empty input
        if not root:
            return ([])
        def recur(node,ch):
            if node.right is not None and node.left is not None:
                ch1=ch+str(node.val)+'->'
                return (recur(node.right,ch1)+recur(node.left,ch1))
            elif node.right is not None:
                ch1=ch+str(node.val)+'->'
                return(recur(node.right,ch1))
            elif node.left is not None:
                ch1=ch+str(node.val)+'->'
                return(recur(node.left,ch1))
            else:
                return([ch+str(node.val)])
        return(recur(root,''))
