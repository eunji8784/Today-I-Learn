import sys

n = int(sys.stdin.readline())
list = [[*sys.stdin.readline().split()] for _ in range(n)]

for i in sorted(list, key=lambda x:x[1]):
  print(i[0], end = ' ')
