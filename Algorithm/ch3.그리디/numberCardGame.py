n, m = map(int, input().split())

result = 0

# 행의 수(n) 만큼 입력받기
for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data) #입력 받은 수에서 가장 작은 값 찾기
  result = max(result, min_value)

print(result)
