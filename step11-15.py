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

# 13 크레인 인형 뽑기 
def solution_13(board, moves): 
  ret = 0
  lanes = [[] for _ in range(len(board[0]))]
  for i in range(len(board) - 1 , -1 , -1):
    for j in range(len(board[0])):
      if board[i][j]:
        lanes[j].append(board[i][j])
  
  bucket = []
  for move in moves:
    lane = lanes[move-1]
    if lane:
      popValue = lane.pop()
      if not bucket:
        bucket.append(popValue)
      else:
        if bucket[-1] == popValue:
          bucket.pop()
          ret += 2
        else:
          bucket.append(popValue)
  return ret
           

board = [
           [0,0,0,0,0]
          ,[0,0,1,0,3]
          ,[0,2,5,0,1]
          ,[4,2,4,4,2]
          ,[3,5,1,3,1]
        ]
moves = [1,5,3,5,1,2,1,4]
print(solution_13(board, moves))

# 14 표 편집
def solution_14(n, k, cmds): 
  ret = "" 
  deleted = []
  up = [i-1 for i in range(n+2)]
  down = [i+1 for i in range(n+1)]
  # print(up)
  # print(down)
  k += 1
 
  for cmd in cmds:
    if 'C' == cmd:
      # 삭제
      deleted.append(k)
      up[down[k]] = up[k]
      down[up[k]] = down[k]
      k = up[k] if n < down[k] else down[k]
    elif 'Z' == cmd:
      # restore
      restore = deleted.pop()
      down[up[restore]] = restore
      up[down[restore]] = restore
    else:
      action, num = cmd.split()
      if action == 'U':
        # 위로
        for _ in range(int(num)):
          k = up[k]
      elif action == 'D':
        # 아래로
        for _ in range(int(num)):
          k = down[k]
    print(up)
    print(down)
    print()

  answer = ["O"] * n 
  for i in deleted:
    answer[i-1] = 'X'
  return "".join(answer)
           
n = 8
k = 2
#cmds = ["C"]
cmds = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution_14(n, k, cmds))

# 15 요새푸스 문제
def solution_15(N, K):

  q = [i for i in range(1,N+1)]
  while len(q) > 1:
    for i in range(K): 
      pop = q.pop(0)
      if K != i+1:
        q.append(pop)

  return q

N = 5
K = 2
print(solution_15(N, K))