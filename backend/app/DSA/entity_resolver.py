class EntityResolver:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self,i):
        if i not in self.parent:
            self.parent[i] = i
            self.rank[i] = 0
            return i
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self,i,j):
        rooti = self.find(i)
        rootj = self.find(j)
        
        if rooti != rootj:
            if self.rank[rooti] < self.rank[rootj]:
                self.parent[rooti] = rootj
            elif self.rank[rooti] > self.rank[rootj]:
                self.parent[rootj] = rooti
            else:
                self.parent[rooti] = rootj
                self.rank[rootj] += 1
            return True
        return False