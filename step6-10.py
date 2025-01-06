# 6 실패율
def solution_6(N, stages):
    ret = [0] * N
    total = len(stages)
    
    for i in range(1, N + 1):
        stage_total = total
        fail_count = 0
        fail_count = stages.count(i)
        print('i', i, 'fail_count : ', fail_count, ' stage_total : ', stage_total)
        if stage_total > 0:
            ret[i - 1] = fail_count / stage_total
        else:
            ret[i - 1] = 0
        
        total -= fail_count

    return ret

# 7 방문길이
keyset = { 'U' : (0,-1), 'D' : (0,1), 'L' : (-1,0), 'R' : (1,0) }
x,y = 5,5

def solution_7(dirs):
  ans = set()
  global x,y
  for dir in dirs:
    nx = x + keyset[dir][0]
    ny = y + keyset[dir][1]
    if not checkLocation(nx,ny):
      continue
    
    ans.add((x,y,nx,ny))
    ans.add((nx,ny,x,y))
    x, y = nx, ny

  return len(ans)/2

def checkLocation(nx,ny):
  return 0 <= nx < 11 and 0 <= ny < 11

# dirs = 'ULURRDLLU'
dirs = 'ULURRDLLU'
print(solution_7(dirs))

# 8 괄호 짝 맞추기
def solution_8(s):
  stack = []
  for c in s:
    if c == '(':
      stack.append(c)
    elif c == ')':
      if not stack:
        return False
      else:
        stack.pop()
  
  if stack:
    return False
  return True

# s = "(())()"
s = "((())()"
print(solution_8(s))

# 9 10진수를 2진수로 변환하기
def solution_9(decimal):
  
  binary = []
  while decimal > 0:
    binary.append(str(decimal % 2))
    decimal = decimal // 2 
    
  binaryStr = ""
  while binary:
    binaryStr += binary.pop()
  return binaryStr

print(solution_9(decimal=13))

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
