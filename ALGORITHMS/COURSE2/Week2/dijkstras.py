from collections import defaultdict
from heapq import *


class Dijkstras:
    def __init__(self, file='test1.txt'):
        self.graph = defaultdict()
        self.vertices = []
        self.edges = set()
        self.total_vertices = 0
        self.total_edges = 0

        self.vertices_processed = []
        self.vertices_unprocessed = []
        self.distance = defaultdict(lambda: float('inf'))

        self.heap_priority_list = []

        if file:
            fp = open(file)
            data = fp.readlines()
            temp_dict = defaultdict(int)
            for foo in data:
                data_row = foo.split()
                temp_dict = {}
                for bar in data_row[1:]:
                    temp_dict[int(bar.split(',')[0])] = int(bar.split(',')[1])
                self.graph[int(data_row[0])] = temp_dict
        self.vertices = self.graph.keys()
        self.total_vertices = len(self.graph.keys())

    '''
    def shortest_path(self, first_vertex=1):
        self.vertices_processed.append(first_vertex)
        self.distance[first_vertex] = 0

        while self.vertices != self.vertices_processed:
            for v in self.vertices:
                print("v", v)
                for w in self.graph[v].keys():
                    if w not in self.vertices_processed:
                        self.distance[v] = min(self.distance[v] +
                                               self.graph[v][w],
                                               self.distance[v])
                self.vertices_processed.append(v)
                # print(self.vertices_processed)
    '''

    def extract_minimum_distance(self):
        v = None
        min_dist = float('inf')
        v = None
        for vertex in self.vertices_unprocessed:
            if self.distance[vertex] < min_dist:
                v = vertex
                min_dist = self.distance[vertex]
        return v

    def shortest_path(self, first_vertex=1):
        self.vertices_unprocessed = list(self.vertices)
        self.distance[first_vertex] = 0

        while self.vertices_unprocessed:
            v = self.extract_minimum_distance()
            # print(v, self.vertices_unprocessed)
            self.vertices_unprocessed.remove(v)
            # print("v", v)
            for w in self.graph[v].keys():
                if w in self.vertices_unprocessed:
                    self.distance[w] = min((self.distance[v] +
                                            self.graph[v][w]),
                                           self.distance[w])
            # print(self.distance)

    def shortest_path_heap(self, first_vertex=1):
        self.vertices_unprocessed = list(self.vertices)
        self.distance[first_vertex] = 0
        heappush(self.heap_priority_list, (0, first_vertex))

        while self.vertices_unprocessed:
            (_, v) = heappop(self.heap_priority_list)
            # print(v, self.vertices_unprocessed)
            if v not in self.vertices_unprocessed:
                continue
                # skip for alredy processed vertices
            self.vertices_unprocessed.remove(v)
            # print("v", v)
            for w in self.graph[v].keys():
                if w in self.vertices_unprocessed:
                    self.distance[w] = min((self.distance[v] +
                                            self.graph[v][w]),
                                           self.distance[w])
                    heappush(self.heap_priority_list, (min((self.distance[v] +
                                                           self.graph[v][w]),
                                                       self.distance[w]), w))
                    # print(self.heap_priority_list)
            # print(self.distance)


if __name__ == '__main__':
    g = Dijkstras(file='DijkstraData.txt')
    # g = Dijkstras()
    # print(g.graph)
    g.shortest_path_heap()
    print(g.distance)
    print()
    print([g.distance[x] for x in [7, 37, 59, 82, 99, 115, 133, 165,
           188, 197]])
    # [2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068]

    '''
    test output:
    1 0 []
    2 1 [2]
    3 2 [2, 3]
    4 3 [2, 3, 4]
    5 4 [2, 3, 4, 5]
    6 4 [8, 7, 6]
    7 3 [8, 7]
    8 2 [8]
    '''
