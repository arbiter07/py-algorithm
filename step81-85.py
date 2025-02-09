# 81 배낭
def solution_81(items, capacity):
  items.sort(key=lambda x: x[1] / x[0], reverse=True)  # 무게 대비 가치가 높은 순 정렬
  total_value = 0

  for weight, value in items:
    if capacity >= weight:
      total_value += value
      capacity -= weight
    else:
      total_value += (value / weight) * capacity  # 남은 공간만큼 가치 비율로 추가
      break  # 배낭이 꽉 차면 종료

  return total_value

items = [(6, 30), (3, 14), (4, 16), (2, 9)]  # (무게, 가치)
capacity = 10
print(solution_81(items, capacity))  # 46.0

# 82 예산
def solution_82(d, budget):
  answer = 0
  sum =0
  sortD=sorted(d)
  for i in sortD:
    if (sum+i)<=budget:
      sum+=i
      answer+=1
  return answer
d = [1,3,2,5,4]
budget = 9
print(solution_82(d, budget))  # 3 

# 83 구명 보트
def solution_83(people, limit) :
  answer = 0
  people.sort()

  a = 0
  b = len(people) - 1
  while a < b :
    if people[b] + people[a] <= limit :
      a += 1
      answer += 1
    b -= 1
  return len(people) - answer

people = [20,50,50,80]
limit = 100
print(solution_83(people, limit))

# 84 귤 고르기
import collections
def solution_84(k, tangerine):
  answer = 0
  cnt = collections.Counter(tangerine)

  for v in sorted(cnt.values(), reverse = True):
    k -= v
    answer += 1
    if k <= 0:
      break
  return answer

k = 6
tangerine = [1,3,2,5,4,5,2,3]
print(solution_84(k, tangerine))

import math

# 85 기지국 건설
def solution_85(N, stations, W):
  result = 0
  location = 1
  idx = 0

  while location <= N:
    if idx < len(stations) and location >= stations[idx] - W:
      location = stations[idx] + W + 1 
      idx += 1
    else:
      location += 2 * W + 1
      result += 1
      
  return result

# 효율성테스트 고려안함
def solution_85_v2(N, stations, W):
  list_N = [0] * N 
  
  for idx in stations:
    list_N[idx - 1] = 1 
    for i in range(1, W + 1):
      if idx - 1 - i >= 0:
        list_N[idx - 1 - i] = 1
      if idx - 1 + i < N:
        list_N[idx - 1 + i] = 1

  strN = ''.join(map(str, list_N))
  not_install = list(filter(None, strN.split('1'))) 

  result = 0
  for section in not_install:
      result += math.ceil(len(section) / (2 * W + 1))

  return result

# 테스트 케이스
N = 16
stations = [9]
W = 2
print(solution_85(N, stations, W))  # 결과: 3