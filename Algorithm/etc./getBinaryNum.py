""" 
문제) 5 < a < 127을 만족하는 자연수 a 중에, 
이진수로 변환하였을 때 가장 많은 1의 개수를 가지는 최솟값 a를 구하시오.
"""

def getBinaryNum(a, list):
  quota, remainder = divmod(a, 2)
  list.append(remainder)
  if quota == 0:
    return list
  else:
    return getBinaryNum(quota, list)

countList = []

for i in range(6, 127):
  remainderList = []
  answer = getBinaryNum(i, remainderList)
  countNum = answer.count(1)
  countList.append([i, countNum])

countList.sort(key=lambda x:(-x[1],x[0]))
print(countList[0][0]) # 63
