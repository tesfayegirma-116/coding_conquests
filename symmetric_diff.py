# print symmetric difference set in ascending order
a = int(input())
b = set(map(int, input().split()))
d = int(input())
d = set(map(int, input().split()))
for i in sorted(list(b.symmetric_difference(d))):
    print(i)
