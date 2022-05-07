## 📌 Counter() 클래스
+ collections 모듈에서 제공하는 클래스
+ 사전(dict) 클래스의 하위 클래스
+ 리스트나 튜플에서 각 데이터가 등장한 횟수를 ```사전 형식```으로 반환
+ 가장 많이 등장한 값부터 내림차순으로 반환

```python
from collections import Counter

list = [4, 4, 6, 5, 7, 7, 7, 8]
ct = Counter(list)
print(ct)

# Counter({7: 3, 4: 2, 6: 1, 5: 1, 8: 1})
```
```python
from collections import Counter

colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
ct = Counter(colors)
print(ct)

# Counter({'blue': 3, 'red': 2, 'green': 1})
```

### 💡 Counter 클래스의 most_common() 메서드
+ Counter()의 결과값을 내림차순으로 정리하여 리스트 안의 튜플로 반환
+ 인자에 숫자를 넣으면 해당하는 수만큼 상위 결과값부터 반환

```python
from collections import Counter

list = [4, 4, 6, 5, 7, 7, 7, 8]
ct = Counter(list)

mc = ct.most_common()
print(mc)

mc = ct.most_common(1) # 상위 결과값 1개만 반환
print(mc)

# [(7, 3), (4, 2), (6, 1), (5, 1), (8, 1)]
# [(7, 3)]
```

```python
from collections import Counter

colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
ct = Counter(colors)

mc = ct.most_common()
print(mc)

mc = ct.most_common(2) # 상위 결과값 2개만 반환
print(mc)

# [('blue', 3), ('red', 2), ('green', 1)]
# [('blue', 3), ('red', 2)]
```
