#beats 55% in speed and 88% and memory
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def backtrack(i,j,ch):
            if len(ch)==2*n:
                ans.append(ch)
                return
            if i==j:
                backtrack(i+1,j,ch+'(')
            elif i<n:
                backtrack(i,j+1,ch+')')
                backtrack(i+1,j,ch+'(')
            else:
                backtrack(i,j+1,ch+')')
        backtrack(0,0,'')
        return(ans)
