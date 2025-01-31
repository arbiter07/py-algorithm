# 56 문자열 내 마음대로 정렬하기
def solution_56(strings, n):
  return sorted(strings, key=lambda x : (x[n], x))
  

strings = ["sun", "bed", "car"]
n = 1
print(solution_56(strings, n))

# 57 정수 내림차순으로 배치하기
def solution_57(n):
  _list = list(str(n))
  return "".join(sorted(_list, key=lambda x : -int(x)))
  
n = 118372
print(solution_57(n))

# 58 K번째 수
def solution_58(arr, command):
  result = []
  for c in command:
    i, j, k = c[0], c[1], c[2]
    result.append(sorted(arr[i-1 : j])[k-1])
    

  return result
  
arr = [1,5,2,6,3,7,4]
command = [ [2,5,3], [4,4,1], [1,7,3] ]
print(solution_58(arr, command))

import functools

# 59 가장 큰 수
def solution_59(arr):
  result = ""
  str_arr = [str(num) for num in arr]

  sorted_num = sorted (
    str_arr, key=functools.cmp_to_key(lambda a, b : compare(a,b)), reverse=True
  )
  return str(int("".join(sorted_num)))

def compare(a, b):
    t1 = a + b
    t2 = b + a

    if t1 > t2:
        return 1  # a가 b보다 앞에 와야 함
    elif t1 < t2:
        return -1  # b가 a보다 앞에 와야 함
    else:
        return 0  # 순서 유지
  
arr = [0,0,0]
print(solution_59(arr))

# 60 튜플
def solution_60(s : str):
  s_arr = s[2:-2].split("},{")
  sort_arr = sorted(s_arr, key=len)

  result = []
  for value in sort_arr:
    c_arr = value.split(",")
    for value in c_arr:
      intValue = int(value)
      if intValue not in result:
        result.append(intValue)

  return result

s = "{{2,1},{2},{2,1,3},{2,1,3,4}}"
print(solution_60(s))