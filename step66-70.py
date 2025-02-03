from collections import Counter
# 66 롤케이크 자르기
def solution_66(s : list):
  result = 0 
  right = Counter(s)
  left = set()
  
  for idx in range(len(s)):
    left.add(s[idx])
    right[s[idx]] -= 1
    if right[s[idx]] == 0:
      right.pop(s[idx])
    if len(left) == len(right):
      result += 1

  return result

s = [1,2,1,3,1,4,1,2]
print(solution_66(s))

# 67 카펫
def solution_67(brown, yellow):
    total = brown + yellow  # 전체 타일 개수

    # 가능한 가로 길이 찾기 (약수 구하기)
    for w in range(3, total + 1):
        if total % w == 0:  # 전체 개수를 나누어 떨어지는 경우 (w * h)
            h = total // w  # 세로 길이 계산
            
            # 조건: 가로가 세로보다 크거나 같아야 함
            if w >= h and (w - 2) * (h - 2) == yellow:
                return [w, h]

print(solution_67(10, 2))  # [4, 3]
print(solution_67(8, 1))   # [3, 3]
print(solution_67(24, 24)) # [8, 6]

# 68 점프와 순간이동
def solution_68(N):
  return bin(N).count("1")

N = 5
print(solution_68(N))  # 2

# 69 캐릭터의 좌표
def solution_69(keyinput, board):

  x_limit = board[0] // 2
  y_limit = board[1] // 2

  # 현재좌표 
  curr_y = 0
  curr_x = 0

  moves = { "up" : (1,0), "down" : (-1,0), "left" : (0, -1), "right" : (0, 1) }

  def isValidMove(move, cy, cx):
    fy = cy + move[0]
    fx = cx + move[1]
    return -y_limit <= fy <= y_limit and -x_limit <= fx <= x_limit
  
  for key in keyinput:
    move_key = moves[key]
    if isValidMove(move_key, curr_y, curr_x):
      curr_y = curr_y + move_key[0]
      curr_x = curr_x + move_key[1]
    

  return [curr_x , curr_y]
  

keyinput = ["down","down","down","down","down"]
board = [7,9]
print(solution_69(keyinput, board))  # 0,-4

# 70 LCS 계산하기
def solution_70(str1: str, str2: str):
  
  m = len(str1)
  n = len(str2)

  dp = [ [0] * (n + 1) for _ in range(m+1) ]
  

  for i in range(1, m+1):
    for j in range(1, n+1):
      if str1[i-1] == str2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

  for i in range(len(dp)):
    print(dp[i])
    
  return dp[m][n]
s1 = "ABCBDAB"
s2 = "BDCAB"
print(solution_70(s1,s2)) # 4 


