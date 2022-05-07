## 📌 append()
+ array.append(x)의 형태로 사용
+ 새로운 요소를 array 맨 오른쪽 끝에 객체로 추가
+ 입력한 값이 리스트와 같은 iterable 자료형이더라도 객체로 저장

```python
nums = [1, 2, 3]
nums.append(4)
print(nums)

nums.append('4')
print(nums)

nums.append([5, 6])
print(nums)

nums.append((5, 6))
print(nums)

# [1, 2, 3, 4]
# [1, 2, 3, 4, '4']
# [1, 2, 3, 4, '4', [5, 6]]
# [1, 2, 3, 4, '4', [5, 6], (5, 6)]
```

## 📌 extend()
+ array.extend(iterable) 형태로 사용
+ 입력한 iterable 자료형의 항목 각각을 array의 끝에 하나씩 추가
+ __인자로 iterable 자료형만 올 수 있음__ (interable 인자가 아닐 경우 TypeError 발생)
+ 보통 interable 인자를 하나씩 꺼내서 배열에 넣고 싶을 때 extend를 사용

```python
nums = [1, 2, 3]
nums.extend([4])
print(nums)

nums.extend(['4'])
print(nums)

nums.extend([5, 6])
print(nums)

nums.extend((7, 8))
print(nums)

# [1, 2, 3, 4]
# [1, 2, 3, 4, '4']
# [1, 2, 3, 4, '4', 5, 6]
# [1, 2, 3, 4, '4', 5, 6, 7, 8]
```

```python
nums = [1, 2, 3]
nums.extend(4)
print(nums)

# TypeError: 'int' object is not iterable
```

## 📌 insert()
+ array.insert(i, x) 형태로 사용
+ array의 원하는 위치 i 앞에 추가할 값 x를 삽입
+ i에 음수를 입력하면 배열의 오른쪽 끝을 기준으로 처리
+ 추가할 값 x는 객체로 추가되며 iterable 자료형이더라도 객체로 저장

```python
nums = [1, 2, 3]
nums.insert(0, 4)
print(nums)

nums.insert(-1, '4') # 끝에서 1번째 전에 추가
print(nums)

nums.insert(len(nums), [5, 6])
print(nums)

nums.insert(len(nums), (7, 8))
print(nums)

# [4, 1, 2, 3]
# [4, 1, 2, '4', 3]
# [4, 1, 2, '4', 3, [5, 6]]
# [4, 1, 2, '4', 3, [5, 6], (7, 8)]
```
