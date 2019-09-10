from collections import defaultdict
import random


class KragerMinCut:
    def __init__(self, file=None):
        self.graph = defaultdict(list)
        self.vertices = []
        self.edges = set()
        self.total_vertices = 0
        self.total_edges = 0
        if not file:
            '''
            self.graph[1] = [2, 3]
            self.graph[2] = [1, 3]
            self.graph[3] = [2, 1]
            self.vertices = self.graph.keys()
            self.total_vertices = len(self.graph.keys())
            self.total_edges = 3
            '''
            self.graph[1] = [2, 3]
            self.graph[2] = [1, 3, 4]
            self.graph[3] = [2, 1, 4]
            self.graph[4] = [2, 3]
            self.total_edges = 5
        else:
            f = open(file)
            for foo in f.readlines():
                line = foo.split()
                self.graph[line[0]] = line[1:]
        self.vertices = self.graph.keys()
        self.total_vertices = len(self.graph.keys())

    def contract_edge(self, vertexa, vertexb):
        self.graph[vertexa] = [foo for foo in self.graph[vertexa] if
                               foo != vertexb]
        self.graph[vertexb] = [foo for foo in self.graph[vertexb] if
                               foo != vertexa]
        self.graph[vertexa].extend(self.graph[vertexb])
        del self.graph[vertexb]
        # print(self.graph)
        for vertex in set(self.graph[vertexa]):
            self.graph[vertex] = [vertexa if foo == vertexb else foo for foo
                                  in self.graph[vertex]]
        self.total_vertices = len(self.graph.keys())
        self.vertices = self.graph.keys()

    def pick_random_vertex(self):
        vertexa = random.choice(list(self.graph.keys()))
        vertexb = random.choice(self.graph[vertexa])
        return vertexa, vertexb

    def min_cut(self):
        while self.total_vertices > 2:
            vertexa, vertexb = self.pick_random_vertex()
            self.contract_edge(vertexa, vertexb)
            # print("random edges with vertices: ", vertexa, vertexb,
            #        self.graph)
        return len(self.graph[vertexa])


if __name__ == '__main__':
    # g = KragerMinCut()
    # print(g.graph, g.total_vertices, g.total_edges, g.vertices)
    # g.contract_edge(3, 2)
    # print(g.graph, g.total_vertices, g.total_edges, g.vertices)
    # g.contract_edge(3, 1)
    # print("min_cut:", g.min_cut())
    # print(g.graph, g.total_vertices, g.total_edges, g.vertices)
    # g = KragerMinCut('KragerMinCut.txt')
    # print(g.min_cut())
    # print(g.graph, g.total_vertices, g.total_edges)

    cuts = []
    for _ in range(100):
        g = KragerMinCut('KragerMinCut.txt')
        cuts.append(g.min_cut())
    print("minimum cut is: ", min(cuts))
