'''
通用并查集，采用rank、pathhalving
'''
class Vertex():#节点
    def __init__(self,value):
        self.value=value
        self.inEdges=set()#入边
        self.outEdges=set()#出边

    def __hash__(self):
        return 0 if not self.value else self.value.__hash__()

    def __eq__(self, other):#value相同则认为是同一个,value允许为空
        # if other==None:
        #     return False
        return not other.value if not self.value else self.value.__eq__(other.value)

    def __str__(self):
        return 'None' if self.value==None else '[vertex:'+str(self.value)+']'

class UnionFind():
    def __init__(self,nodes):
        self.parents ={}
        self.rank = {}
        for node in nodes:
            self.parents[node]=node
            self.rank[node]=1

    def is_same(self,v1,v2):
        return not v2 if not v1 else self.find(v1).__eq__(self.find(v2))

    def union(self,v1,v2):
        p1=self.find(v1)
        p2=self.find(v2)
        r1=self.rank[p1]
        r2=self.rank[p2]
        if r1<r2:
            self.parents[p1]=p2
        elif r1>r2:
            self.parents[p2]=p1
        else:#相等的时候才需要修改rank
            self.parents[p1]=p2
            self.rank[p2]=r2+1

    def find(self, v):#path havling 每隔一个节点指向祖父节点
        while not v.__eq__(self.parents[v]):
            self.parents[v]=self.parents[self.parents[v]]
            v=self.parents[v]
        return v

    def __str__(self):
        result=''
        for item in self.parents.keys():
            result+=('['+str(item)+' parent:'+str(self.parents.get(item))+' rank:'+str(self.rank.get(item))+']\n')
        return result

if __name__ == '__main__':
    verteces={}
    for i in range(10):
        vertex=Vertex(i)
        verteces[i]=vertex
    union_find=UnionFind(verteces.values())
    union_find.union(Vertex(0),Vertex(1))
    union_find.union(Vertex(2),Vertex(3))
    union_find.union(Vertex(0),Vertex(2))
    print(union_find)
    union_find.find(Vertex(0))
    print(union_find)
    print(union_find.is_same(Vertex(0),Vertex(1)))
    print(union_find.is_same(Vertex(0),Vertex(9)))



