# avarage of all the plants in her greenhouse
def average(array):
    # return avarge of all the plants in her greenhouse
    a = set((array))
    b = sum(a)
    return b/len(a)


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)
