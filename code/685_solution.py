class UnionFind(object):
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1] * n

    def find(self, i):
        while i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])  
            i = self.parents[i]
        return i

    def union(self, p, q):
        root_p, root_q = map(self.find, (p, q))
        if root_p == root_q: return False
        small, big = sorted([root_p, root_q], key=lambda x: self.sizes[x])
        self.parents[small] = big
        self.sizes[big] += self.sizes[small]       
        return True
    

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        in_degrees = collections.Counter([edge[1] for edge in edges])
        edges = list(filter(lambda edge: in_degrees[edge[1]] == 1, edges)) +\
                list(filter(lambda edge: in_degrees[edge[1]] == 2, edges))
        n = len(edges) + 1
        uf = UnionFind(n)
        for edge in edges:
            if (not uf.union(edge[0], edge[1])): return edge
        return edge