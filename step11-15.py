# 11 짝지어 제거하기
def solution_11(s):
  stack = []
  for c in s:
    if not stack:
     stack.append(c)
    else:
      if c == stack[-1]:
        stack.pop()
      else:
        stack.append(c)
  return (not stack) * 1

print(solution_11(s="baabaa"))

# 12 주식가격 
def solution_12(s): 
  ret = []
  for i, c in enumerate(s):
    cnt = 0
    for index in range(i+1,len(s)):
      cnt += 1
      if c > s[index]:
        break
    ret.append(cnt)
  return ret

print(solution_12(s=[1,2,3,2,3])) # [4,3,1,1,0]