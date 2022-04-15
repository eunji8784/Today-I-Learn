## 📌 break
+ 가장 가까운 ```반복문```을 벗어나기 위해 사용
+ break가 호출되면 뒷 줄에 코드가 아직 남아있어도 해당 반복문을 즉시 탈출
```python
num = 0

while 1:
  print(num)
  if num == 5:
    break
  num += 1
  
>>
0
1
2
3
4
5
```

## 📌 return
+ 해당 ```함수```에서 벗어나기 위해 사용
+ 역시 뒷 줄에 코드가 있더라도 반환값을 반환하고 해당 함수를 즉시 탈출
```python
def sum(a, b):
    return a+b

s = sum(2, 3)
print s

>> 5
```

## 📌 continue
+ break와 다르게 반복문 자체를 벗어나지 않고 반복문 내의 ```작업문```을 벗어나기 위해 사용
+ continue가 호출되면 뒷 줄의 코드를 수행하지 않고 해당 반복문을 다시 실행
```python
num = 0

while num < 5:
  num += 1
  if num == 3:
    continue
  print(num)
  
>>
1
2
4
5
```
