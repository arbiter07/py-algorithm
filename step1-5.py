# 1 역정렬된 새로운 배열 반환
def solution_1(arr):
  sorted_list = list(sorted(arr))
  return sorted_list

# 2 중복제거
def solution_2(arr):
  arr = list(set(arr))

# 3 두개 뽑아서 더하기
def solution_3(arr):
  ret = []
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      print(i,j)
      ret.append(arr[i] + arr[j])
  ret = sorted(set(ret))
  return ret
 
 # 4 수포자 모의고사
def solution_4(answer):
  # pattern 
  patterns = [
    [1,2,3,4,5]
    ,[2,1,2,3,2,4,2,5]
    ,[3,3,1,1,2,2,4,4,5,5]
  ]
  score = [0] * 3
  for i, answer in enumerate(answer):
    for j, pattern in enumerate(patterns):
      if answer == pattern[i % len(pattern)]:
        score[j] += 1
  
  max_score = max(score)
  highest_score = []
  for i, score in enumerate(score):
    if score==max_score:
      highest_score.append(i+1)
  return highest_score

# 5 행렬의 곱셈
def solution_5(arr1, arr2):
  r1, c1 = len(arr1), len(arr1[0])
  r2, c2 = len(arr2), len(arr2[0])
  
  ret = [[0] * c2 for _ in range(r1)]
  
  for i in range(r1): # 3
    for j in range(c2): # 2
      for k in range(c1): # 3 
        ret[i][j] += arr1[i][k] * arr2[k][j]
  return ret

print(solution_5([[1,4],[3,2],[4,1]], [[3,3],[3,3]]))