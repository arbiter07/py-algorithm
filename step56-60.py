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