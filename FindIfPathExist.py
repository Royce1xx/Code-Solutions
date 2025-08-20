from collections import deque
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        royce = [[] for l in range(n)]

        for u, v in edges:
            royce[u].append(v)
            royce[v].append(u)

        if source ==  destination:
            return True
            
        q = deque([source])
        visit = {source}

        while q:
            u = q.popleft()
            if u ==  destination:
                return True
            for v in royce[u]:
                if v not in visit:
                    visit.add(v)
                    q.append(v)
        return False
    
    
        
       