class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        #bellman-ford algorithm
        min_dist = [float('inf') for i in range(n)] 
        min_dist[src] = 0
        for u,v,w in flights:
            if u == src:
                min_dist[v] = w

        for i in range(K):
            temp = min_dist[::]
            for u,v,w in flights:
                if min_dist[u] + w < temp[v]:
                    temp[v] = min_dist[u] + w
            min_dist = temp
                        
        #no need to detect for negative cycles since all positive weights
        if min_dist[dst] == float('inf'):
            return -1
        else:
            return min_dist[dst]
