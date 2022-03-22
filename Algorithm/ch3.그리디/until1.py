n, k = map(int, input().split())

count = 0
quota = 0

while n != 1:
  if n % k == 0:
    quota = n // k
    count += 1
    n = quota
  else:
    n -= 1
    count += 1

print(count)
