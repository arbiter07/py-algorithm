
def dfs(idx, graph, visited):
  visited[idx] = True
  print(idx, end = ' ')
  for next in range(N + 1):
    if not visited[next] and graph[idx][next]:
      dfs(next ,graph ,visited)

def bfs(q, graph, visited):
  while q:
    curr = q.pop(0)
    print(curr, end=' ')
    for next in range(1, N+1):
      if not visited[next] and graph[curr][next]:
        visited[next] = True
        q.append(next)

def solution(N, M, V):

  graph = [[ False ] * (N + 1) for _ in range(N+1) ]
  visited = [ False ] * (N + 1)

  for line in M:
    a,b = line[0], line[1]
    graph[a][b] = True
    graph[b][a] = True
  
  # DFS
  dfs(V, graph, visited)

  print()
  # BFS
  visited = [ False ] * (N + 1)
  q = [V]
  visited[V] = True
  bfs(q, graph, visited)

  return True

N = 4
M = [(1,2) , (1,3) , (1,4) , (2,4) , (3,4)]
V = 1
solution(N, M, V)