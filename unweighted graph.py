n = int(input())
d = {}
for i in range(n):
    a,b = map(int,input().split())
    d[a] = d.get(a,[]) + [b]
    d[b] = d.get(b,[]) + [a]
start = int(input())
end = int(input())
def countpaths(d,visited,start,end,c):
    if start == end:
        print(visited)
        return c + 1
    for i in d[start]:
        if i not in visited:
            c = countpaths(d,visited.union({i}),i,end,c)
    return c

def minlengthpath(d,visited,start,end,c,final):
    if start == end:
        return len(visited)
    for i in d[start]:
        if i not in visited:
            final = min(final,minlengthpath(d,visited.union({i}),i,end,c+1,final))
    return final

def bfs(d,visited,start):
    q = [start]
    while q:
        k = q.pop(0)
        for i in d[k]:
            if i not in visited:
                visited.add(i)
                q.append(i)
    return visited

print(bfs(d,{start},start))