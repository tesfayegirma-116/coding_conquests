#Print the sum of the elements of set  on a single line.
n = int(input())
s = set(map(int, input().split()))

#number of commands
m = int(input())

#loop through commands
for i in range(m):
    #split command
    command = input().split()
    #check command
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))

print(sum(s))