# 51
# 52
# 53
# 54 계수 정렬 구현하기
def solution_54(s):
  
  count = [0 for _ in range(26)]
  
  for c in s:
    count[ ord(c) - ord('a') ] += 1

  sorted_str = ""
  for i in range(26):
    if count[i] != 0:
      sorted_str += chr(i + ord('a')) * count[i]
  
  return sorted_str
  

s = "hello"
print(solution_54(s))

# 55 정렬이 완료된 두 배열 합치기(병합정렬)
def solution_55(arr1, arr2):

  merged = []
  i, j = 0,0

  while len(arr1) > i and len(arr2) > j:
    if arr1[i] <= arr2[j]:
      merged.append(arr1[i])
      i += 1
    else:
      merged.append(arr2[j])
      j += 1

  print(i , j)
  print(len(arr1), len(arr2))
  while i < len(arr1):
    merged.append(arr1[i])
    i += 1
  while j < len(arr2):
    merged.append(arr2[j])
    j += 1
  
  return merged
  

arr1 = [1,3,5]
arr2 = [2,4,6]
print(solution_55(arr1, arr2))