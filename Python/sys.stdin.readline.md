## 💡 sys.stdin.readline()
+ input()과 같은 파이썬 입력 방식 중 하나 (* _input(): 파이썬에서 제공하는 내장 함수_)
+ 반복문으로 여러 줄 입력받는 경우 input()은 시간초과가 발생할 수 있음
+ return 타입은 __문자열__
+ 시간초과 방지를 위해 ```sys.stdin.readline()```으로 쓰는 습관을 들이자
```
- sys 모듈은 Python 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
- stdin은 Python 인터프리터가 표준 입력에 사용하는 파일 객체, readline()은 파일 객체의 메소드 중 하나로 read(), readlines() 와 같이 파일 객체를 읽을 때 사용

즉, sys.stdin.readline() 은 sys 라는 모듈의 파일 객체 stdin 의 메소드 중 readline() 을 사용한다는 의미이다
readline() 은 입력을 읽을 때 한 번에 한 줄씩 읽는데, 이 말은 여러 줄의 입력이 있을 때 한 줄을 읽고 나면 그 다음 줄을 가리킨다는 뜻
```
출처: https://velog.io/@ecvheo1/%EC%9E%85%EB%A0%A5-%EB%B0%9B%EB%8A%94-%EB%B0%A9%EB%B2%95-sys.stdin.readline, https://developeryuseon.tistory.com/90


### 📌 정수 입력받을 땐 int로 변환 필요
+ ```sys.stdin.readline()```은 한 줄 단위로 입력받기 때문에 개행문자가 같이 포함됨. _ex) 3 -> 3\n_
```python
import sys
n = int(sys.stdin.readline())
```
+ 정수형 변환과 함께 개행문자도 제거됨

### 📌 n줄의 문자열을 입력받아 리스트에 저장하는 경우
+ ```strip()```으로 문자열 맨 왼쪽과 오른쪽의 공백문자를 제거
```python
import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for _ in range(n)]
```

#### ➕ strip()
+ ```strip([chars])``` : 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거
+ ```lstrip([chars])``` : 인자로 전달된 문자를 String의 왼쪽에서 제거
+ ```rstrip([chars])``` : 인자로 전달된 문자를 String의 오른쪽에서 제거
