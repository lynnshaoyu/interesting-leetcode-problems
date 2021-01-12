from collections import defaultdict
from heapq import *

class Solution(object):
    def getManhattanDist(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return abs(x2-x1) + abs(y2-y1)
    
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Straightforward application of Prim's algorithm for Minimum Spanning Trees.
        
        # First, build out adjacency list representing graph, where every node can reach
        # every other node with weight of Manhattan Dist between the two nodes
        adj_list = defaultdict(set)
        for i, point1 in enumerate(points):
            for j, point2 in enumerate(points):
                if i != j:
                    dist = self.getManhattanDist(point1, point2)
                    adj_list[i].add((dist, j))
                    adj_list[j].add((dist, i))
                    
        # First step in Prim's: initialize all keys for nodes to infinity, except
        # source node which can be any in this case.
        key_value = [float('inf') for point in points]
        key_value[0] = 0
        
        # min_heap stores (edge_weight, next_neighboring_node). 
        # in_MST stores nodes already included in MST.
        min_heap = []
        heappush(min_heap, (0, 0))
        in_MST = set()
        total_dist = 0
        
        while len(in_MST) != len(points):
            current_dist, ind = heappop(min_heap)
            if ind not in in_MST:
                in_MST.add(ind)
                total_dist += current_dist
                next_nodes = adj_list[ind]
                for node_dist, node_ind in next_nodes:
                    if node_dist < key_value[node_ind]:
                        key_value[node_ind] = node_dist
                        heappush(min_heap, (node_dist, node_ind))

        return total_dist
            
        
