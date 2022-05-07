## 📌 min()
+ 인수로 받은 자료형 내에서 최소값을 찾아서 반환하는 함수
+ min(x)에서 x는 __iterable__ 한 자료형
+ __iterable__: 반복이 가능한 데이터 타입 즉, member를 하나씩 반환(접근)할 수 있는 데이터 타입. ex) 리스트, 튜플, 문자열

```python
array = [4, 6, 7, 9, 2, 1]
print(min(array))
print(type(min(array)))

# 1
# <class 'int'>
```
+ 비교 데이터들 간 타입이 같아야함
```python
array = ['4', 6, 7, 9, 2, 1]
print(min(array))
print(type(min(array)))

# TypeError: '<' not supported between instances of 'int' and 'str'
```
+ 람다식 사용 가능
```python
a = [1, 2, 3, 4, 5]
 
b = min(a, key=lambda x: x % 2)
print(b)

# 2
```

```python
str = "Hello_World"
print(min(str))
print(type(min(str)))

# H
# <class 'str'>
```

```python
str = "Hello_W2orld"
print(min(str))
print(type(min(str)))

# 2
# <class 'str'>
```

+ 두 개 이상의 인자를 받을 수 있음
+ 인자 간의 데이터 타입이 같아야 함

```python
a = [1, 2, 3] 
b = [4, 5, 6] 
print(min(a, b))
print(type(min(a, b)))

# [1, 2, 3]
# <class 'list'>
```
```python
a = 'BlockDMask' 
b = 'BAAAlockDMask' 
print(min(a, b))
print(type(min(a, b)))

# BAAAlockDMask
# <class 'str'>
```

## 📌 max()
+ 인수로 받은 자료형 내에서 최대값을 찾아서 반환하는 함수
+ mix() 함수와 사용법 같음

출처: https://blockdmask.tistory.com/411
