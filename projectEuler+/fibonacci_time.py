def fib(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib(n-1, computed) + fib(n-2, computed)
    return computed[n]


def fibeven(n):
    fibarr = [0, 1]
    i = 2
    while fib(i) < n:
        fibarr.append(fib(i))
        i += 1
    return sumevenfib(fibarr)


def sumevenfib(fibarr):
    sumevenfib = 0
    for num in fibarr:
        if num % 2 == 0:
            sumevenfib += num
    return sumevenfib


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(fibeven(n))
