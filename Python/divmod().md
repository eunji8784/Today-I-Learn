## 📌 divmod
+ 정수의 나눗셈에서 ```몫```과 ```나머지```를 구해주는 함수
+ 정수를 나눈 몫과 나머지를 __튜플__ 형식으로 반환  

- 함수 사용 없이 구하는 경우
  ```python
  a = 10
  b = 3
  print(a//b, a%b)
  # 3 1
  ```
  
- divmod 함수를 사용해서 구하는 경우
  ```python
  a = 10
  b = 3
  print(divmod(a, b))
  print(*divmod(a, b)) # unpacking
  # (3, 1)
  # 3 1
  ```
  ```python
  a, b = divmod(10, 3) # unpacking
  print(a, b)
  # 3 1
  ```
  
  + divmod를 사용하는게 무조건 좋은 것은 아님
  + 작은 수를 다룰 때는 a//b, a%b 형식이 좋고, 큰 수를 다룰 때 divmod가 성능 면에서 좋음
