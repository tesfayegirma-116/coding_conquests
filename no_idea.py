# No Idea in python - Hacker Rank Solution
io = input().split()
n = int(io[0])
m = int(io[1])

storage = list()
count = 0

storage = list(map(int, input().strip().split()))

A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))

for i in storage:
    if i in A:
        count += 1
    if i in B:
        count -= 1
print(count)





