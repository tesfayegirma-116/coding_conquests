def multipleof3_5(n):
    P3 = (n-1) // 3
    P5 = (n-1) // 5
    P15 = (n-1) // 15
    Sum = 3 * (P3 + 1) * P3 // 2 + 5 * (P5 + 1) * \
        P5 // 2 - 15 * (P15 + 1) * P15 // 2
    return Sum


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(multipleof3_5(n))
