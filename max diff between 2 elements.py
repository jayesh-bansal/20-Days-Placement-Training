arr = list(map(int,input().split()))
mini = float('inf')
final = 0
for i in arr:
    mini = min(mini,i)
    final = max(i - mini,final)
print(final)