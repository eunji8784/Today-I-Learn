## 📍 isalpha()
+ 문자열의 구성이 모두 알파벳인지 확인하는 함수
+ 문자열에 숫자 및 공백, 특수문자가 포함되어 있으면 False를 반환
+ 한글 지원
```python
ex1 = 'A'
ex2 = 'ABC'
ex3 = '안녕'
ex4 = 'Hello World'
ex5 = '1004Hello'
ex6 = 'Hello~!'

print(ex1.isalpha()) # True
print(ex2.isalpha()) # True
print(ex3.isalpha()) # True
print(ex4.isalpha()) # False
print(ex5.isalpha()) # False
print(ex6.isalpha()) # False
```

## 📍 isdigit()
+ 문자열의 구성이 모두 숫자인지 확인하는 함수
+ 공백이나 특수문자가 포함되면 False를 반환
```python
ex1 = '1'
ex2 = '123'
ex3 = '안녕'
ex4 = 'Hello'
ex5 = '010-1234-5678'
ex6 = '123 456'

print(ex1.isdigit()) # True
print(ex2.isdigit()) # True
print(ex3.isdigit()) # False
print(ex4.isdigit()) # False
print(ex5.isdigit()) # False
print(ex6.isdigit()) # False
```

## 📍 isalnum()
+ 문자열이 알파벳 또는 숫자인지 확인하는 함수
+ 공백이나 특수문자가 포함되면 False를 반환
```python
ex1 = '123'
ex2 = 'Hello'
ex3 = '123Hello'
ex4 = '123 Hello'
ex5 = '123-Hello'

print(ex1.isalnum()) # True
print(ex2.isalnum()) # True
print(ex3.isalnum()) # True
print(ex4.isalnum()) # False
print(ex5.isalnum()) # False
```
