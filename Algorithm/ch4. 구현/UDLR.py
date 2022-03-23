n = int(input())
plan = input().split()

x,y = 1

for direction in plan:
  if direction == 'L':
    if y - 1 > 1:
      y -= 1
  elif direction == 'R':
    if y + 1 < n:
      y += 1
  elif direction == 'U':
    if x - 1 > 1:
      x -= 1
  else:
    if x + 1 < n:
      x += 1

print(x, y)

# n = int(input())
# plans = input().split()

# x, y = 1, 1
# plans_type = ['L', 'R', 'U', 'D']
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# for plan in plans:
#   for i in range(len(plans_type)):
#     if plan == plans_type[i]:
#       nx = x + dx[i]
#       ny = y + dy[i]
#   if nx < 1 or nx > n or ny < 1 or nx > n:
#     continue
#   x, y = nx, ny

# print(x, y)
      
      
