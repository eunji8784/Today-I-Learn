## 💡 sys.stdin.readline()
+ input()과 같은 파이썬 입력 방식 중 하나
+ 반복문으로 여러 줄 입력받는 경우 input()은 시간초과가 발생할 수 있음
+ return 타입은 __문자열__
+ 시간초과 방지를 위해 ```sys.stdin.readline()```으로 쓰는 습관을 들이자

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
