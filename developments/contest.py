'''
n = int(input())
data = [int(i) for i in input().split()]
data =[]
for i in range(n):
    data.extend(input())

with open('input.txt') as file:
    n = file.readline().strip()
    data = file.readline().strip()


if len(set(data)) > 2:
    print('-1')
else:
    print(max(data) - min(data))

n = int(input())
data = [int(i) for i in input().split()]
data = data[:n]

if len(set(data)) > 2:
    print(-1)
else:
    print(max(data) - min(data))


n = int(input())
Volumes = list(map(int, input().split()))
answer = 0
maximal = Volumes[0]

for i in range(len(Volumes)):
    maximal = max(Volumes[i], maximal)
    if Volumes[i] < maximal:
        answer = -1
        break

print(max(Volumes) - min(Volumes) if answer == 0 else answer)
'''
n = int(input())
side_position = []
for i in range(n):
    row = input()
    side_position.append(row)


n = int(input())
reqs = []
for i in range(n):
    reqs.append(input().split())

print(side_position)
print(reqs)

def func(side_pos, reqs):
    for req in reqs:
        count = req[0]
        side = req[1]
        pos = req[2]
        for string in side_pos:

            if side == 'left':
                side = '0:3'
                if pos == 'window': pos = 0
                else: pos = 2
            else:
                side = '4:7'
                if pos == 'window': pos = 6
                else: pos = 4



            if '.' in string[side] >= count and string[pos] == '.':
                return 'TRUE'
            else:
                return 'FALSE'

print(func(side_position, reqs))


#print(reqs)
#print(side_position)
