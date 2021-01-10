from collections import defaultdict
from heapq import *

class Solution(object):
    def mostSimilar(self, n, roads, names, targetPath):
        """
        :type n: int
        :type roads: List[List[int]]
        :type names: List[str]
        :type targetPath: List[str]
        :rtype: List[int]
        """
        #we use a modification of djikstra's algorithm to find the
        #min edit distance path
        graph = defaultdict(set)
        for edge in roads:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        previous_city = [[None for i in range(len(targetPath))] for city in range(n)]
        min_dist = [[float('inf') for i in range(len(targetPath))] for city in range(n)]
        min_heap = []

        for i in range(n):
            min_dist[i][0] = 0 if names[i] == targetPath[0] else 1
            heappush(min_heap, (min_dist[i][0], i, 0))

        min_dist_found, min_city_found = None, None

        while len(min_heap) != 0:
            dist, city_index, path_index = heappop(min_heap)
            if path_index == len(targetPath) - 1:
                min_dist_found = dist
                min_city_found = city_index
                break
            next_index = path_index + 1
            for next_city in graph[city_index]:
                new_dist = dist
                if names[next_city] != targetPath[next_index]:
                    new_dist += 1
                if new_dist < min_dist[next_city][next_index]:
                    min_dist[next_city][next_index] = new_dist
                    previous_city[next_city][next_index] = city_index
                    heappush(min_heap, (new_dist, next_city, next_index))

        ind = len(targetPath) - 1
        city = min_city_found
        path = [city]
        while previous_city[city][ind] is not None:
            prev_city = previous_city[city][ind]
            path.append(prev_city)
            city = prev_city
            ind -= 1

        return reversed(path)
