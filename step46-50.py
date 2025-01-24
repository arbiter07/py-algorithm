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