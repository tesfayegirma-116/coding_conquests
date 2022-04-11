# divmod
from unittest import result


a = int(input())
b = int(input())

result = divmod(a, b)
print('{}\n{}'.format(result[0], result[1]))
print(result)
