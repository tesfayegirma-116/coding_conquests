from collections import namedtuple

N = int(input())
fields = input().split()

total = 0
for i in range(N):
    students = namedtuple('student', fields)
    student = students(*input().split())
    total += int(student.MARKS)

print('{:.2f}'.format(total / N))



