# 46 전력망을 둘로 나누기
def solution_46(N, wires):
  # 인접행렬 행렬은 좌표가 있는경우에 사용 효율성이 리스트보다 많이 떨어짐
  graph_yx = [ [ 0 for _ in range(N+1) ] for _ in range(N+1) ]

  # 인접리스트
  graph_list = [ [] for _ in range(N+1) ]
  
  result = []
  for v in wires:
    y,x = v[0], v[1]
    graph_yx[y][x] = 1
    graph_yx[x][y] = 1
    graph_list[x].append(y)
    graph_list[y].append(x)
  
  def dfs_list(idx, visited):
    # result length로 개수 확인할 수 있음
    result.append(idx)
    cnt = 1
    visited[idx] = True
    for v in graph_list[idx]:
      if not visited[v]:
        cnt += dfs_list(v, visited)
    return cnt
  def dfs_graph(idx, visited):
    cnt = 1
    visited[idx] = True
    for idx, value in enumerate(graph_yx[idx]):
      if not visited[idx] and value == 1:
        cnt += dfs_graph(idx, visited)
    return cnt
  
  def bfs(start, visited):
    q = [start]
    visited[start] = True
    cnt = 1
    while q:
      curr = q.pop(0)
      for v in graph_list[curr]:
        if not visited[v]:
          q.append(v)
          visited[v] = True
          cnt += 1
    return cnt
  min_diff = 100
  for i, v in enumerate(wires):
    visited = [False for _ in range(N+1)]
    y,x = v[0], v[1]
    graph_yx[y][x] = 0
    graph_yx[x][y] = 0
    graph_list[x].remove(y)
    graph_list[y].remove(x)
    result = []
    size_1 = bfs(1, visited)
    size_2 = N - size_1
    
    if max(size_1, size_2) - min(size_1, size_2) < min_diff:
      min_diff = max(size_1, size_2) - min(size_1, size_2)
    

    # 마지막에 복구
    graph_yx[y][x] = 1
    graph_yx[x][y] = 1
    graph_list[x].append(y)
    graph_list[y].append(x)
    
  return min_diff

N = 9
wires = [
         [1,3]
        ,[2,3]
        ,[3,4]
        ,[4,5]
        ,[4,6]
        ,[4,7]
        ,[7,8]
        ,[7,9]
      ]
print(solution_46(N, wires)) # 

# 47 백트래킹 기본 1~N 까지의 수를 조합하여 10을 만들기
def solution_47(N):
  result = []
  cnt = [0]
  def backtrack(sum, selected_nums, start):
    print(sum, selected_nums)
    cnt[0] += 1
    if sum == 10:
      print(' --',True)
      result.append(selected_nums)
      return

    for i in range(start, N+1):
      if sum + i <= 10:
        backtrack( sum + i , selected_nums + [i] , i+1 ) 
  
  backtrack(0,[],1)
  print(cnt)
  return result

N = 5
print(solution_47(N))

# backtrack(0, [], 1) # sum=0, selected_nums=[]

#   i = 1
#   backtrack(1, [1], 2) # sum=1, selected_nums=[1]
  
#     i = 2
#     backtrack(3, [1, 2], 3) # sum=3, selected_nums=[1, 2]
    
#       i = 3
#       backtrack(6, [1, 2, 3], 4) # sum=6, selected_nums=[1, 2, 3]
      
#         i = 4
#         backtrack(10, [1, 2, 3, 4], 5) # sum=10, selected_nums=[1, 2, 3, 4]
#           # sum == 10 -> result.append([1, 2, 3, 4])
        
#       i = 5
#       backtrack(11, [1, 2, 3, 5], 6) # sum=11, invalid -> return
      
#     i = 4
#     backtrack(7, [1, 2, 4], 5) # sum=7, selected_nums=[1, 2, 4]
    
#       i = 5
#       backtrack(12, [1, 2, 4, 5], 6) # sum=12, invalid -> return

#     i = 5
#     backtrack(8, [1, 2, 5], 6) # sum=8, selected_nums=[1, 2, 5]

#   i = 3
#   backtrack(4, [1, 3], 4) # sum=4, selected_nums=[1, 3]
  
#     i = 4
#     backtrack(8, [1, 3, 4], 5) # sum=8, selected_nums=[1, 3, 4]
    
#     i = 5
#     backtrack(9, [1, 3, 5], 6) # sum=9, selected_nums=[1, 3, 5]

#   i = 4
#   backtrack(5, [1, 4], 5) # sum=5, selected_nums=[1, 4]

#     i = 5
#     backtrack(10, [1, 4, 5], 6) # sum=10, selected_nums=[1, 4, 5]
#       # sum == 10 -> result.append([1, 4, 5])

#   i = 5
#   backtrack(6, [1, 5], 6) # sum=6, selected_nums=[1, 5]

# i = 2
# backtrack(2, [2], 3) # sum=2, selected_nums=[2]

# 48

# 49 피로도 
def solution_49(k, dungeons):
  visited = [False for _ in range(len(dungeons))]

  def dfs(k, cnt, visited):
    print(k, cnt, visited)
    result = cnt
    for idx, value in enumerate(dungeons):
      if value[0] <= k and not visited[idx]:
        visited[idx] = True
        result = max(result, dfs(k-value[1], cnt + 1, visited))
        visited[idx] = False
    return result

  return dfs(k, 0, visited)

k = 80
# 최소필요도, 소모 피로도
dungeons = [ [80,20], [50,40], [30,10] ]
print(solution_49(k, dungeons)) # 3

# 50 N-Queen
def solution_50(n):
	
  def getAns(n, y , width, d1 ,d2):
    ans = 0
    # 모든 행을 통과한 경우
    if y == n:
      ans += 1
    else:
      # 현재 행에서 퀸이 놓일 수 있는 모든 위치를 시도
      for i in range(n):
        # 대각선이나 해당열에 놓을 수 없는경우
        print('i , y , n', i , y, n)
        if width[i] or d1[i + y] or d2[i - y + n]:
          continue
        width[i] = d1[i + y] = d2[i - y + n] = True
        ans += getAns(n, y+1, width, d1, d2)
        width[i] = d1[i + y] = d2[i - y + n] = False
    return ans

  ans = getAns(
          n
          , 0
          , [False] * n # 열
          , [False] * (n* 2 ) # 대각선 1
          , [False] * (n* 2 ) # 대각선 2
        )
  return ans
n = 4
print(solution_50(n)) # 2

  # (0,0) (0,1) (0,2) (0,3)
  # (1,0) (1,1) (1,2) (1,3)
  # (2,0) (2,1) (2,2) (2,3)
  # (3,0) (3,1) (3,2) (3,3)