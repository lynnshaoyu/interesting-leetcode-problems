class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        #floyd warshall used here 
        
        min_dist = [[float('inf') for i in range(n)] for j in range(n)]
        for i in range(n):
            min_dist[i][i] = 0
        for edge in edges:
            min_dist[edge[0]][edge[1]] = edge[2]
            min_dist[edge[1]][edge[0]] = edge[2]
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    new_dist = min_dist[i][k] + min_dist[k][j]
                    if new_dist < min_dist[i][j]:
                        min_dist[i][j] = new_dist
        city_counts = [0 for i in range(n)]
        
        for i in range(n):
            for j, dist in enumerate(min_dist[i]):
                if dist <= distanceThreshold and j != i:
                    city_counts[i] += 1
        
        min_city_count = min(city_counts)
        for i in range(len(city_counts)-1, -1, -1):
            if city_counts[i] == min_city_count:
                return i
