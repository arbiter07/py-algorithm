# 75 정수삼각형
def solution_75(triangle : list):
  result = 0
  
  dp = [[ 0 for _ in range(len(triangle)) ] for _ in range(len(triangle)) ]

  dp[0][0] = triangle[0][0]
  dp[1][0] = triangle[1][0] + dp[0][0]
  dp[2][0] = triangle[2][0] + dp[0][0]

  for i in range(2, len(triangle)): # 2 3 4
    for j in range(len(triangle[i])): # 1 2 3 4 5
      dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]


  print(dp[len(triangle)-1])

  return max(dp[len(triangle)-1])

triangle = [ [7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5] ]
print(solution_75(triangle)) # 30
