#total number of distinct countries
a = int(input())
s = set()

for i in range(a):
    n = str(set(input()))
    s.add(n)
print(len(s))
