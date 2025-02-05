import math

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


###########################
# template
# 
def solution():
    return 0
print(solution())
