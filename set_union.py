#total number of student subscriptions

n = int(input())
subscribed_e = set(map(int, input().split()))

b = int(input())
subscribed_f = set(map(int, input().split()))

total = subscribed_e.union(subscribed_f)

print(len(total))