# 16 기능 개발
def solution_16(progresses, speeds):
  ret = []
  execute_days = [] 
  # 7 3 9
  
  for i, v in enumerate(progresses):
    day = 0
    while v < 100:
      v += speeds[i]
      day+=1
    execute_days.append(day)

  while len(execute_days) > 0:
    pop = execute_days.pop(0)
    group = 1
    while len(execute_days) > 0:
      next = execute_days[0]
      if pop >= next:
        execute_days.pop(0)
        group +=1
      else: 
        break
    ret.append(group)

  return ret

# progresses = [93,30,55]
# speeds = [1,30,5]

progresses = [95,90,99,99,80,99]
speeds = [1,1,1,1,1,1]
print(solution_16(progresses, speeds))

# 17 카드뭉치
def solution_17(cards1, cards2, goal):

  for _ in range(len(goal)):
    c = goal[0]
    if cards1 and c==cards1[0]:
      cards1.pop(0)
      goal.pop(0)
    elif cards2 and c==cards2[0]:
      cards2.pop(0)
      goal.pop(0)
    else:
      break
  print(goal)
  return "Yes" if not goal else "No"

cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
print(solution_17(cards1, cards2, goal))

# 18 두 개의 수로 특정값 만들기
def count_sort(arr, k):
  hashtable = [0] * (k+1)
  
  for num in arr:
    if num<=k:
      hashtable[num] = 1
  return hashtable
  

def solution_18(arr, target):

  hashtable = count_sort(arr, target)
  print(hashtable)

  for num in arr:
    complement = target - num
    if(
      complement is not num
      and complement > 0 
      and complement <= target
      and hashtable[complement] == 1
    ):
      return True  
  return False

arr = [1,2,3,4,8]
target = 6
print(solution_18(arr, target))

# 19 문자열 해싱을 이용한 검색 함수 만들기
def polynomial_hash(str):
  p = 31 
  m = 1_000_000_007
  hash_value = 0
  for char in str:
    hash_value = (hash_value * p + ord(char)) % m
  return hash_value

def solution_19(string_list, query_list):
  p = 31 
  m = 1_000_000_007

  hash_list = [polynomial_hash(str) for str in string_list]
  print(hash_list)
  
  result = []

  for query in query_list:
    query_hash = polynomial_hash(query)
    if query_hash in hash_list:
      result.append(True)
    else:
      result.append(False)

  return result

string_list = ["apple", "banana", "cherry"]
query_list = ["banana", "kiwi", "melon", "apple"]
print(solution_19(string_list, query_list))

# 20 완주하지 못한 선수
def solution_20(participant, completion):

  dic = {}
  for p in participant:
      if p in dic.keys():
         dic[p] += 1
      else:
        dic[p] = 1
  for c in completion:
      dic[c] -= 1
  
  print(dic)
  for key in dic.keys():
     if dic[key] > 0:
        return key

  return ""

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution_20(participant, completion)) # leo