from itertools import permutations

a, b = [int(x) if x.isnumeric() else x for x in input().upper().split()]
ans = list(permutations(a, b))
ans.sort()

for i in ans:
    print("".join(i))
