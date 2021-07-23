'''
List Graph 采用邻接表实现的图，实际上是邻接表和逆邻接表的组合十字链表
'''
import heapq
from typing import Set
from queue import Queue,LifoQueue
from Graph import Graph
from UnionFind import UnionFind
from functools import total_ordering

class UndirectedListGraph(Graph):
    def __init__(self):
        self.vertices={}#采用哈希表map存储所有节点
        self.edges=set()#采用集合set存储所有边

    def verticesSize(self):
        return len(self.vertices)

    def edgesSize(self):
        return len(self.edges)

    def addVertex(self,v=None):
        """
        :param v:velue
        """
        if v in self.vertices.keys():return
        self.vertices[v]=UndirectedListGraph.Vertex(v)

    def removeVertex(self,v):
        # the vertext to be removed doesn't exist
        if v not in self.vertices.keys():return
        vertex_delete=self.vertices.get(v)
        for edge in vertex_delete.outEdges:
            self.edge.to.inEdges.remove(edge)
            self.edges.remove(edge)
        for edge in vertex_delete.inEdges:
            self.edge.fro.outEdges.remove(edge)
            self.edges.remove(edge)
        del(self.vertices[v])


    def addEdge(self,fro,to,weight=None):
        """
        :param fro:value of start node
        :param to: value of end node
        :param weight: edge weight
        """
        from_vertex=self.vertices.get(fro)
        #if the nodes in the edge don't exit, create them at first
        if not from_vertex:
            from_vertex=UndirectedListGraph.Vertex(fro)
            self.vertices[fro]=from_vertex
        to_vertex=self.vertices.get(to)
        if not to_vertex:
            to_vertex=UndirectedListGraph.Vertex(to)
            self.vertices[to]=to_vertex
        # now from and to is absolutely exist
        edge1=UndirectedListGraph.Edge(from_vertex,to_vertex,weight)
        edge2=UndirectedListGraph.Edge(to_vertex,from_vertex,weight)
        # if the edge is already exist, delete the original edge
        if edge1 in self.edges:
            from_vertex.outEdges.remove(edge1)
            to_vertex.inEdges.remove(edge1)
            self.edges.remove(edge1)

        if edge2 in self.edges:
            from_vertex.outEdges.remove(edge2)
            to_vertex.inEdges.remove(edge2)
            self.edges.remove(edge2)
        # add the edge with new weight
        from_vertex.outEdges.add(edge1)
        from_vertex.inEdges.add(edge2)
        to_vertex.outEdges.add(edge2)
        to_vertex.inEdges.add(edge1)
        self.edges.add(edge1)
        self.edges.add(edge2)

    def removeEdge(self,fro,to):
        out_vertex = self.vertices.get(fro)
        if out_vertex==None:return
        in_vertex = self.vertices.get(to)
        if in_vertex==None:return
        edge=UndirectedListGraph.Edge(fro,to)
        if edge not in self.edges:return
        out_vertex.outEdges.remove(edge)
        in_vertex.inEdges.remove(edge)
        self.edges.remove(edge)

    def showGraph(self):
        for vertex in self.vertices.values():
            print(vertex)
            print('out--------------')
            str_out=""
            for i in vertex.outEdges:
                str_out+=str(i)+' '
            print('None' if len(str_out)==0 else str_out)
            print('in--------------')
            str_in=""
            for i in vertex.inEdges:
                str_in+=str(i)+' '
            print('None' if len(str_in)==0 else str_in)
        print('tatol edges : ')
        for edge in self.edges:
            print(edge)
        print()

    def bfs(self,v):#广度优先搜索
        print('breadth first search----------------')
        vertex=self.vertices.get(v)
        if vertex==None:return
        q=Queue()
        visited_v_set=set()
        q.put(vertex)
        visited_v_set.add(vertex)
        while not q.empty():
            vertex=q.get()
            print(vertex)
            for edge in vertex.outEdges:
                to_v=self.vertices.get(edge.to)
                if to_v in visited_v_set:
                    continue
                else:
                    q.put(to_v)
                    visited_v_set.add(to_v)

    def dfs_inner(self, vertex, set_v):
        if vertex==None:return
        print(vertex.value)
        set_v.add(vertex)
        for edge in vertex.outEdges:
            if edge.to in set_v:
                continue
            else:
                self.dfs_inner(edge.to,set_v)

    def dfs(self,v):
        print('depth first search with recursion----------------')
        vertex=self.vertices.get(v)
        if vertex==None:return
        self.dfs_inner(vertex,set())

    def dfs_nonrecursion(self,v):
        print('depth first search without recursion----------------')
        start_vertex=self.vertices.get(v)
        visited_vertex=set()#已访问顶点集合
        stack = LifoQueue()  # 创建栈
        #将顶点入栈，表示访问该节点，打印value
        stack.put(start_vertex)
        print(start_vertex.value)
        visited_vertex.add(start_vertex)
        while not stack.empty():
            vertex=stack.get()#出栈，对该节点的子节点进行访问
            for edge in vertex.outEdges:
                if edge.to in visited_vertex:#已访问节点
                    continue
                else:
                    print(edge.to.value)#访问子节点内容
                    visited_vertex.add(edge.to)
                    stack.put(vertex)#父节点与子节点入栈
                    stack.put(edge.to)
                    break

    def mst(self)-> Set[Graph.EdgeInfo]:#可以选择prim算法或者cruskal算法
        return self.kruskal()

    def kruskal(self)-> Set[Graph.EdgeInfo]:
        edge_set=set()#the edges set spanning the mst
        edge_heap=[edge for edge in self.edges]#generate data list
        heapq.heapify(edge_heap)
        union_find=UnionFind(self.vertices.values())#vertices中存储了所有的顶点v->Vertex(v)
        edge_size=len(self.vertices)-1#the edge num that mst need
        while len(edge_heap)>0 and len(edge_set)<edge_size:
            edge=heapq.heappop(edge_heap)
            if union_find.is_same(edge.fro,edge.to):
                continue
            else:
                union_find.union(edge.fro,edge.to)
                #保存Graph中定义的通用边类型
                edge_set.add(Graph.EdgeInfo(edge.fro.value,edge.to.value,edge.weight))

        return edge_set

    class Vertex():#节点
        def __init__(self,value):
            self.value=value
            self.inEdges=set()#入边
            self.outEdges=set()#出边

        def __hash__(self):
            return 0 if self.value==None else self.value.__hash__()

        def __eq__(self, other):#value相同则认为是同一个,value允许为空
            return not other.value if not self.value else self.value.__eq__(other.value)

        def __str__(self):
            return 'None' if not self.value else str(self.value)

    @total_ordering
    class Edge():#边
        def __init__(self,fro,to,weight=1):
            self.fro=fro
            self.to=to
            self.weight=weight

        def __hash__(self):
            return 31*self.fro.__hash__()+self.to.__hash__()

        def __eq__(self, other):#two edges which have the same from and to node is considered same
            return self.fro.__eq__(other.fro) and self.to.__eq__(other.to)

        def __str__(self):
            return "Edge [from=" + str(self.fro) + ", to=" + str(self.to) + ", weight=" + str(self.weight) + "]"

        def __le__(self, other):  # 小于等于
            return self.weight <= other.weight

def graph_one():
    graph = UndirectedListGraph()
    # generate edges
    graph.addEdge(0, 4, 6)
    graph.addEdge(1, 0, 9)
    graph.addEdge(1, 2, 3)
    graph.addEdge(2, 0, 2)
    graph.addEdge(2, 3, 5)
    graph.addEdge(3, 4, 1)
    graph.showGraph()
    # graph.removeEdge(0,4)
    # graph.removeVertex(3)
    # graph.showGraph()
    # graph.bfs(2)
    # graph.bfs(1)
    # graph.bfs(3)
    graph.dfs(1)
    # graph.dfs(2)
    graph.dfs_nonrecursion(1)

def graph_two():
    graph=UndirectedListGraph()
    graph.addEdge('A','B')
    graph.addEdge('B','C')
    graph.addEdge('B','D')
    graph.addEdge('B','E')
    graph.addEdge('C','E')
    graph.addEdge('D','E')
    graph.addEdge('E','F')
    # graph.addEdge('F','C')
    graph.showGraph()

def mst_test():
    graph = UndirectedListGraph()
    graph.addEdge('A', 'B',4)
    graph.addEdge('A', 'H',8)
    graph.addEdge('B', 'C',8)
    graph.addEdge('B', 'H',11)
    graph.addEdge('C', 'I',2)
    graph.addEdge('C', 'D',7)
    graph.addEdge('C', 'F',4)
    graph.addEdge('H', 'I',7)
    graph.addEdge('H', 'G',1)
    graph.addEdge('I', 'G',6)
    graph.addEdge('D', 'E',9)
    graph.addEdge('D', 'F',14)
    graph.addEdge('G', 'F',2)
    graph.addEdge('F', 'E',10)
    edge_set=graph.mst()
    for edge in edge_set:
        print(edge)

if __name__=='__main__':
    mst_test()

