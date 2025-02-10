def solution_46(N, wires):

  graph_list = [ [] for _ in range(N + 1) ]
  for x, y in wires:
    graph_list[x].append(y)
    graph_list[y].append(x)


  min = float("inf")
  for x,y in wires:
    graph_list[x].remove(y)
    graph_list[y].remove(x) 

    visited = [0] * (N+1)

    cnt = bfs(1, visited, graph_list)
    diffcnt = N-cnt
    
    if min > abs(diffcnt - cnt):
      min = abs(diffcnt - cnt)

    graph_list[x].append(y)
    graph_list[y].append(x) 

    
  return min

def bfs(start, visited, graph_list):
  cnt = 1 
  visited[start] = 1
  q = [start]

  while q:
    node = q.pop()
    for next in graph_list[node]:
      if not visited[next]:
        visited[next] = 1
        q.append(next)
        cnt += 1


  return cnt

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