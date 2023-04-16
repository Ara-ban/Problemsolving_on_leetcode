#to reformulate the problem, it's about finding whether the directed graph of course dependancies
#is acyclic or not, one way to do it is to try to construct the topological order of the graph
#that is only possible if the graph is acyclic
#beats 47% in speed and 96% in memory
from collections import deque
from collections import defaultdict
class Solution:
    def canFinish(self, numcourses: int, preq: List[List[int]]) -> bool:
        def topo(adj,l):
            dep=[0]*l
            for q in adj.values():
                for i in q:
                    dep[i]+=1
            q=deque()
            for i in range(l):
                if dep[i]==0:
                    q.append(i)
            order=[]
            while q:
                x=q.popleft()
                order.append(x)
                for i in adj[x]:
                    dep[i]-=1
                    if dep[i]==0:
                        q.append(i)
            return order
        adj=defaultdict(list)
        for link in preq:
            adj[link[1]].append(link[0])
        return len(topo(adj,numcourses))==numcourses
