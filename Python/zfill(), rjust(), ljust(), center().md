## 📌 zfill() 메서드
+ zfill(width: int)
+ 문자열 앞을 __0__ 으로 채우고 싶을 때 사용
+ 인수는 자릿수를 의미 (integer)
+ 반환 타입은 ```string```이며 문자열로만 사용 가능 (다른 타입을 넣으면 에러 발생)
+ 원본 문자열은 바뀌지 않음

```python
str = 'abcd'

print(str.zfill(6))
print(type(str.zfill(6)))
print(str)

# 00abcd
# <class 'str'>
# abcd
```

## 📌 rjust(), ljust(), center() 메서드
+ (width, [fillchar])
+ 문자열 앞을 __원하는 문자__ 로 채우고 싶을 때 사용
+ 반환 타입은 ```string``` 이며 마찬가지로 문자열로만 사용 가능
+ ```rjust()```: 오른쪽 기준 정렬
+ ```ljust()```: 왼쪽 기준 정렬
+ ```center()```: 가운데 정렬
+ 두 번째 인자에 아무 값도 넣지 않았을 경우에는 공백으로 처리
+ 원본 문자열은 바뀌지 않음

```python
str = 'abcd'
print(str.rjust(6))
print(str.ljust(6))
print(str.center(6))

print(str.rjust(6, '0'))
print(str.ljust(6, '0'))
print(str.center(6, '0'))

print(str.rjust(6, '*'))
print(str.ljust(6, '*'))
print(str.center(6, '*'))

#   abcd
# abcd  
#  abcd 
# 00abcd
# abcd00
# 0abcd0
# **abcd
# abcd**
# *abcd*
```

### ❗ 두 번째 인자에는 하나의 문자만 넣어야 함
```python
print(str.rjust(6, '*-'))

# TypeError: The fill character must be exactly one character long
```

## ➕ format()을 이용해 문자열 말고 정수로 사용하기
+ 기본은 왼쪽 기준 정렬
+ 반환 타입은 ```string```
```python
print(format(123, '4'))
print(format(123, '04'))
print(format(123, '10'))
print(format(123, '010'))

print(type(format(123, '05')))

print('{0:4d}'.format(123))
print('{0:04d}'.format(123))
print('{0:10d}'.format(123))
print('{0:010d}'.format(123))

print(type('{0:05d}'.format(123)))

#  123
# 0123
#        123
# 0000000123
# <class 'str'>
#  123
# 0123
#        123
# 0000000123
# <class 'str'>
```

참고: https://codingpractices.tistory.com/39
