from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(lambda: -1)

for i in range(1, n+1):
    word = input()
    d[word] = d[word] + ' ' + str(i) if word in d else str(i)

for _ in range(m):
    print(d[input()])
