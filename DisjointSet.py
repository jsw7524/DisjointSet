

class DisjointSet(object):
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.n=n

    def FindRoot(self,x):
        if self.parent[x] == x:
            return x
        else:
            return self.FindRoot(self.parent[x])

    def Union_Sets(self,x,y):
        root1=self.FindRoot(x)
        root2=self.FindRoot(y)

        if root1 == root2:
            return

        if self.size[root1] > self.size[root2]:
            self.parent[root2]=root1
            self.size[root1]+=self.size[root2]
        else:
            self.parent[root1]=root2
            self.size[root2]+=self.size[root1]

    def Same_Set(self,x,y):
        return self.FindRoot(x)==self.FindRoot(y)


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ds=DisjointSet(1001)
        for u,v in edges:
            if ds.Same_Set(u,v):
                return [u,v]
            else:
                ds.Union_Sets(u,v)
        return


sln=Solution()
assert [2,3]==sln.findRedundantConnection([[1,2], [1,3], [2,3]])
assert [1,4]==sln.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]])
