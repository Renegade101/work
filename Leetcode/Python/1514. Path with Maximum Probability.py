import heapq
from collections import defaultdict


class Solution(object):
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.2]
    start = 0
    end = 2
    def maxProbability(n, edges, succProb, start, end):
        maps = defaultdict(list)
        for i in range(len(edges)):
            maps[edges[i][0]].append((edges[i][1], succProb[i]))
            maps[edges[i][1]].append((edges[i][0], succProb[i]))
        q = [(-1, start)]
        dist = defaultdict(float)
        dist[start] = -1
        while q:
            curdist, cur = heapq.heappop(q)
            if cur == end:
                return -curdist
            for node, prob in maps[cur]:
                tmp = curdist * prob
                if tmp < dist[node]:
                    dist[node] = tmp
                    heapq.heappush(q, (tmp, node))
        return 0
    print(maxProbability(n, edges, succProb, start, end))