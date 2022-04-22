import sys

n = int(sys.stdin.readline())
list = [[*sys.stdin.readline().split()] for _ in range(n)]

for j in range(len(list)):
  list[j][1] = int(list[j][1])

for i in sorted(list, key=lambda x:x[1]):
  print(i[0], end = ' ')
