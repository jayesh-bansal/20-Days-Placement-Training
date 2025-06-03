from collections import defaultdict
from collections import deque
import heapq
d = defaultdict(list)
for _ in range(int(input())):
    a,b,w = map(int,input().split())
    d[a] += [[b,w]]
    d[b] += [[a,w]]

def minpath(d,visited,start,end,s):
    if end == start:
        return s
    m = float('inf')
    for i,j in d[start]:
        if i not in visited:
            m = min(m,minpath(d,visited.union({i}),i,end,s+j))
    return m

def dijkstra(values,route,start):
    q = deque([start])
    visited = set()
    while q:
        k = q.popleft()
        if k not in visited:
            for i,j in values[k]:
                route[i] = min(route[i],route[k]+j)
                q.append(i)
        visited.add(k)

def krushgaltree():
    arr = [list(map(int,input().split())) for i in range(int(input()))]
    heap = heapq.heapify(arr)
    visited = set()
    m = 0
    for i,j in heap:
        if i not in visited:
            m += i
            visited.add(j)
    return m

def primsalgo():
    heap = [0,0]
    visited = set()
    m = 0
    while heap:
        w,u = heapq.heappop(heap)
        if u not in visited:
            visited.add(u)
            m += w
            for i,j in d[u]:
                if i not in visited:
                    heapq.heappush(heap,[j,i])
    return m

start = int(input())
temp = {}
for i in d:
    temp[i] = float('inf')
temp[start] = 0
dikstra(d,temp,start)
print(temp)