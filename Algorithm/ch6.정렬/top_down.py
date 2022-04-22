import sys

n = int(sys.stdin.readline())
list = [int(sys.stdin.readline()) for _ in range(n)]

for i in sorted(list, reverse = True):
  print(i, end = ' ')
