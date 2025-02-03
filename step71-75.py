# 71 LIS 계산하기
def solution_71(nums : list):
  result = 0 

  n = len(nums)
  dp = [1] * n

  for i in range(1,n):
    for j in range(n):
      if nums[i] > nums[j]:
        dp[i] = max(dp[i], dp[j]+1)
      print(dp)

  return max(dp)
nums = [1,4,2,3,1,5,7,3]
dpdp = [1,2,1,1,1,1,1,1]
print(solution_71(nums)) # 5

# 72

# 73 피보나치 수
def solution_73(n):

  dp = [0] * n
  dp[0] = 1
  dp[1] = 1

  def getFibo(n):
    if dp[n] == 0:
      return getFibo(n-1) + getFibo(n-2)
    else:
      return dp[n]
  
  return getFibo(n-1)

def solution_73_v2(n):

  dp = [1,1]

  for i in range(2, n):
    dp.append(dp[i-1] + dp[i-2])
  
  return dp[n-1]
n = 8
print(solution_73(n)) # 5 // 1 1 2 3 5 8 13 21
print(solution_73_v2(n)) # 5 // 1 1 2 3 5 8 13 21

# 74 2xn 타일링
def solution_74(n):

  if n == 1:
    return 1
  elif n == 2:
    return 2
  
  dp = [0 for _ in range(n)]
  dp[0] = 1
  dp[1] = 2
  for i in range(2, n):
      dp[i] = (dp[i - 1] + dp[i - 2])% 1000000007
  return dp[n-1]

n = 4
print(solution_74(n))

# 75 정수삼각형
def solution_75(triangle : list):
  result = 0
  
  dp = [[ 0 for _ in range(len(triangle)) ] for _ in range(len(triangle)) ]

  dp[0][0] = triangle[0][0]
  dp[1][0] = triangle[1][0] + dp[0][0]
  dp[1][1] = triangle[1][1] + dp[0][0]
  

  for i in range(2, len(triangle)): # 2 3 4
    for j in range(len(triangle[i])): # 1 2 3 4 5
      if j == 0:
        dp[i][j] += dp[i-1][j] + triangle[i][j]
      elif j == len(triangle[i]) - 1:
        dp[i][j] += dp[i-1][j-1] + triangle[i][j]
      else:
        dp[i][j] += max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]


  return max(dp[len(triangle)-1])

triangle = [ [7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5] ]
print(solution_75(triangle)) # 30
