# 76 땅따먹기
def solution_76(land):

  for i in range(1,len(land)):
    for j in range(len(land[i])):
      land[i][j] += max(land[i-1][:j] + land[i-1][j+1:] )

  return max(land[len(land)-1])

land = [ [1,2,3,5], [5,6,7,8], [1,1,21,1] ]

print(solution_76(land))

# 77 도둑질
def solution_77(money):
    if len(money) == 1:
        return money[0]
    
    # 첫 번째 집을 털수도 있는 경우 (마지막 집 제외)
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    
    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
    
    # 첫 번째 집을 안 터는 경우 (마지막 집 포함)
    dp2 = [0] * len(money)
    dp2[0] = 0  # 첫 번째 집 안 털기 때문에 0
    dp2[1] = money[1]
    
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
    
    
    print(dp1)
    print(dp2)

    return max(dp1[-2], dp2[-1])  # 두 경우 중 최댓값 반환

money = [ 1,2,3,5,5 ]

print(solution_77(money)) # 4 

# 78 가장 큰 정사각형
def solution_78(board):
    
  row = len(board)
  col = len(board[0])

  for i in range(1, row):
    for j in range(1, col):
       if board[i][j] == 1:
          board[i][j] = min(
             board[i-1][j]
             ,board[i][j-1]
             ,board[i-1][j-1]
          ) + 1
  
  result = 0
  for i in range(row):
    for j in range(col):
       result = max(board[i][j] , result)
  return result ** 2
board = [
     [0,1,1,1]
    ,[1,1,1,1]
    ,[1,1,1,1]
    ,[0,0,1,0]
]	
print(solution_78(board)) # 9

# 79 단어퍼즐 