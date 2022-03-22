// 받은 돈 입력받기
n = int(input())
count = 0

// 동전 단위
coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += n // coin
  n %= coin

print(count)
