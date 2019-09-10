import bisect
from collections import defaultdict, deque
import sys, threading
# sys.setrecursionlimit(2**20)
# threading.stack_size(67108864)
import resource

sys.setrecursionlimit(1000000)

resource.setrlimit(resource.RLIMIT_STACK, (2**21, 2**22))


class SCC:
    def __init__(self, file='scc_test.txt'):
        self.graph = defaultdict(list)
        self.graph_reversed = defaultdict(list)
        self.total_vertices = 0
        self.total_edges = 0
        self.explored_vertices = []

        f = open(file)
        for foo in f.readlines():
            line = foo.split()
            # self.graph[line[0]].append(line[1])
            bisect.insort_left(self.graph[int(line[0])], int(line[1]))
            bisect.insort_left(self.graph_reversed[int(line[1])], int(line[0]))
            self.total_edges += 1
        self.vertices = self.graph.keys()
        self.total_vertices = len(self.graph.keys())
        self.curLabel = 0
        self.fvalue = defaultdict(int)
        self.t = 0
        self.s = None
        self.scc_leader = defaultdict(list)

    def dfs_recursion(self, s):
        self.explored_vertices.append(s)
        for vertex in self.graph.get(s):
            if vertex not in self.explored_vertices:
                self.dfs_recursion(vertex)

    def dfs_iteration(self, s):
        stack = [s]
        while stack:
            v = stack.pop()
            if v not in self.explored_vertices:
                self.explored_vertices.append(v)
                for vertex in self.graph.get(v)[::-1]:
                    stack.append(vertex)
                    # print(stack)

    def bfs_iteration(self, s):
        queue = deque([s])
        while queue:
            v = queue.popleft()
            if v not in self.explored_vertices:
                self.explored_vertices.append(v)
                for vertex in self.graph.get(v):
                    queue.append(vertex)
                    # print(queue)

    def bfs_recursion(self, s):
        if isinstance(s, int):
            queue = [s]
        elif not s:
            return
        else:
            queue = s
        new_queue = []
        for v in queue:
            if v not in self.explored_vertices:
                self.explored_vertices.append(v)
                new_queue.extend(self.graph.get(v))
        self.bfs_recursion(new_queue)

    def toposort(self):
        self.curLabel = self.total_vertices
        for v in self.vertices:
            if v not in self.explored_vertices:
                self.dfs_topo(v)

    def dfs_topo(self, v):
        self.explored_vertices.append(v)
        for vertex in self.graph.get(v):
            if vertex not in self.explored_vertices:
                self.dfs_topo(vertex)
        self.fvalue[v] = self.curLabel
        self.curLabel -= 1

    def reverse_graph(self):
        self.graph_reversed = defaultdict(list)
        for key, values in self.graph.items():
            for value in values:
                # print(key, value)
                self.graph_reversed[value].append(key)

    def kosaraju_dfs_loop(self, graph):
        self.t = 0
        self.explored_vertices = []
        self.scc_leader = defaultdict(list)
        for i in range(len(self.vertices), 0, -1):
            if i not in self.explored_vertices:
                # print(i)
                self.s = i
                self.kosaraju_dfs(graph, i)

    def kosaraju_dfs(self, graph, i):
        self.explored_vertices.append(i)
        self.scc_leader[self.s].append(i)
        if graph.get(i):
            for vertex in graph.get(i):
                if vertex not in self.explored_vertices:
                    # print(vertex)
                    self.kosaraju_dfs(graph, vertex)
        self.t += 1
        self.fvalue[i] = self.t
        # print(self.fvalue)

    def kosaraju(self):
        # self.reverse_graph()
        # print(scc.graph_reversed)
        self.kosaraju_dfs_loop(self.graph_reversed)
        new_graph = defaultdict(list)
        for foo in self.graph:
            new_graph[self.fvalue[foo]].extend([self.fvalue[bar] for bar in
                                                self.graph[foo]])
        # print("new_graph", new_graph)
        self.kosaraju_dfs_loop(new_graph)

    def top_5_SCC(self):
        l = [len(values) for key, values in self.scc_leader.items()]
        l = sorted(l)[::-1]
        print(l[:5])


if __name__ == '__main__':
    '''
    scc = SCC()
    print(scc.graph, scc.total_edges, scc.total_vertices)
    scc.dfs_recursion(1)
    print(scc.explored_vertices)
    scc = SCC()
    scc.dfs_iteration(1)
    print(scc.explored_vertices)
    scc = SCC()
    scc.bfs_iteration(1)
    print(scc.explored_vertices)
    scc = SCC()
    scc.bfs_recursion(1)
    print(scc.explored_vertices)
    scc = SCC()
    scc.toposort()
    print(scc.fvalue)
    '''

    '''
    scc = SCC()
    print(scc.graph, scc.total_edges, scc.total_vertices)
    scc.reverse_graph()
    # print(scc.graph_reversed)
    scc.toposort()
    print(scc.fvalue)
    '''
    scc = SCC(file='SCC.txt')
    # print(scc.graph, scc.total_edges, scc.total_vertices)
    scc.kosaraju()
    # print(scc.fvalue)
    # print(scc.scc_leader)
    scc.top_5_SCC()
