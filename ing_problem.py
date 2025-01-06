# 10 괄호 회전하기
def solution_10(s):
  ret = 0  
  for _ in enumerate(s):
    if isValid(s):
      ret += 1
    s = s[1:] + s[:1]
  return ret 

def isValid(s):
  stack = []
  for c in s:
    if c == '(' or c == '{' or c == '[':
      stack.append(c)
    else:
      if not stack:
        return False
      
      if (c == ')' and stack[-1] == '('):
        stack_c = stack.pop()
      elif (c == ']' and stack[-1] == '['):
        stack_c = stack.pop()
      elif (c == '}' and stack[-1] == '{'):
        stack_c = stack.pop()
      else:
        return False

  return not stack
solution_10(s="[](){}")
