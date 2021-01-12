from collections import deque, defaultdict
from heapq import *

class Solution(object):
    def __init__(self):
        self.node_to_set_map = defaultdict(int)
        self.disjoint_sets = defaultdict(set)
        self.set_count = 0
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Use Kruskal algorithm where instead of edge weights (all edges effectively have weight
        # 1 here) we use the edge's index in given list edges as weight. Therefore, we 
        # choose later edges last. 
        mst_edges = []
        disjoint_sets = {}
        
        min_heap = []
        
        def put_node_in_disjoint_sets(node):
            self.node_to_set_map[node] = self.set_count
            self.disjoint_sets[self.set_count] = set([node])
            self.set_count += 1
        def merge_sets(node1, node2):
            node1_set_no = self.node_to_set_map[node1]
            node2_set_no = self.node_to_set_map[node2]
            new_set = self.disjoint_sets[node1_set_no].union(self.disjoint_sets[node2_set_no])
            self.disjoint_sets[node1_set_no] = new_set
            del self.disjoint_sets[node2_set_no]
            for elem in new_set:
                self.node_to_set_map[elem] = node1_set_no
            
        for i, edge in enumerate(edges):
            heappush(min_heap, (i, edge))
            u, v = edge
            if u not in self.node_to_set_map:
                put_node_in_disjoint_sets(u)
            if v not in self.node_to_set_map:
                put_node_in_disjoint_sets(v)
        
        while len(mst_edges) < len(edges):
            weight, edge = heappop(min_heap)
            node1, node2 = edge
            if self.node_to_set_map[node1] == self.node_to_set_map[node2]:
                return edge
            else:
                mst_edges.append(edge)
                merge_sets(node1, node2)
                
            
