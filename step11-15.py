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
