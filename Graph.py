'''
基类 Graph
'''
from typing import Set


class Graph():
    def __init__(self):
        return

    def verticesSize(self):
        return

    def edgesSize(self):
        return

    def addVertex(self,v):
        """
        :param v:velue
        :return:
        """
        return

    def removeVertex(self,v):
        return

    def addEdge(self,fro,to,weight=None):
        print('2')
        return

    def removeEdge(self,fro,to):
        return

    class EdgeInfo():
        def __init__(self,fro,to,weight):
            self.fro=fro
            self.to=to
            self.weight=weight

        def __str__(self):
            return '[fro:'+str(self.fro)+' to:'+str(self.to)+' weight:'+str(self.weight)+']'

    def mst(self)-> Set[EdgeInfo]:#minimum spanning tree 最小生成树
        return set()



class UnionFind():
    def __init__(self,nodes):
        self.parents ={}
        self.rank = {}
        for node in nodes:
            self.parents[node]=node
            self.rank[node]=1

    def is_same(self,v1,v2):
        return self.find(v1) == self.find(v2)

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
        while not self.parents[v].__eq__(v):
            parent=self.parents[v]
            grand=self.parents[parent]
            self.parents[v]=grand#指向祖父节点
            self.rank[parent]-=1
            if not parent.__eq__(grand):
                self.rank[grand]-=1
            v=grand
        return v