## 💡 리스트를 역순으로 출력하는 방법
### 1) 리스트 슬라이싱 사용
+ 리스트[::-1], 리스트[-1::-1], 리스트[len(리스트)-1::-1]
+ 순서를 뒤집은 리스트를 반환
+ __원본 리스트는 바뀌지 않음__
```python
list = [1, 2, 4, 6, 3, 7]
print(list[::-1])
# print(list[-1::-1])
# print(list[len(list)-1::-1])
print(list)

# [7, 3, 6, 4, 2, 1]
# [1, 2, 4, 6, 3, 7]
```
### 2) reverse() 메서드 사용
+ 반환값이 없음
+ __원본 리스트를 변경함__
```python
list = [1, 2, 4, 6, 3, 7]
print(list.reverse())
print(list)

# None
# [7, 3, 6, 4, 2, 1]
```

### 3) reversed() 내장함수 사용
+ reversed()는 주어진 시퀀스 (리스트, 튜플 등)에 대해 순서가 뒤집어진 __iterator 객체__ 를 반환
+ 따라서 내장함수 list() 사용해 리스트로 변환해야 함
+ __원본 리스트는 바뀌지 않음__
```python
data = [1, 2, 4, 6, 3, 7]
print(type(reversed(data)))
print(list(reversed(data)))
print(data) 

# <class 'list_reverseiterator'>
# [7, 3, 6, 4, 2, 1]
# [1, 2, 4, 6, 3, 7] 
```
