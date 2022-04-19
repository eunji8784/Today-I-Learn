## 📌 sort()와 sorted()의 차이
+ __sort()__
  + 리스트에서 제공하는 기본 ```메서드```
  + _리스트.sort()_ 의 형식으로 사용
  + 원본 리스트 자체를 변경함
  + 반환값이 없음
  + 리스트에서만 사용 가능

```python
list1 = [4, 2, 3, 5, 1]
list2 = list1.sort()
print(list1)
print(list2)

# [1, 2, 3, 4, 5]
# None
```

+ __sorted()__
  + 파이썬의 ```내장 함수```
  + _sorted(리스트)_ 의 형식으로 사용
  + 원본 리스트를 수정하지 않고 정렬된 새로운 리스트를 반환함
  + 어떠한 리터러블 객체도 인자로 받을 수 있음. ex) 딕셔너리
  
```python
list1 = [4, 2, 3, 5, 1]
list2 = sorted(list1)
print(list1)
print(list2)

# [4, 2, 3, 5, 1]
# [1, 2, 3, 4, 5]
```
```python
# 딕셔너리 정렬
dic = {
    2: 1,
    3: 4,
    5: 2,
    1: 3,
    4: 1
}
x = sorted(dic.items(), key=lambda x:x[0])
print(x)

# [(1, 3), (2, 1), (3, 4), (4, 1), (5, 2)]
```
#### :bulb: sort()와 sorted() 둘 다 매개변수로 key와 reverse를 받을 수 있음.
