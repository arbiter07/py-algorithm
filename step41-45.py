# 41
# 42 게임 맵 최단거리
def solution_42(maps):
  
  dir = [ (0, -1), (0, 1), (1, 0), (-1, 0) ]
  distances = [[ float("inf") for _ in range(len(maps[0])) ] for _ in range(len(maps))]
  result = bfs([0,0] , maps, distances, dir)
  return -1 if result == float("inf") else result 

def bfs(start, maps, distances, dir):

  q = [start]
  distances[start[0]][start[1]] = 1
  N = len(maps)
  M = len(maps[0])

  while q:
    y, x = q.pop(0)
    for ay, ax in dir:
      ny, nx = y + ay , x + ax
      # 좌표 벗어나거나 막혀있음
      if 0 > ny or ny >= N or 0 > nx or nx >= M or maps[ny][nx] == 0:
        continue
      if distances[ny][nx] > distances[y][x] + 1:
        q.append([ny, nx])
        distances[ny][nx] = distances[y][x] + 1

  return distances[N-1][M-1]

maps = [
         [1,0,1,1,1]
        ,[1,0,1,0,1]
        ,[1,0,1,1,1]
        ,[1,1,1,0,1]
        ,[0,0,0,0,1]
      ]
print(solution_42(maps))



# 43 네트워크 // dfs bfs 
def solution_43_DFS2(n, computers):
    result = 0
    visited = [False for _ in range(n)]  # 방문 여부를 저장하는 리스트

    def dfs(i):
        visited[i] = True  # 현재 노드를 방문 처리
        for j, connected in enumerate(computers[i]):  # 해당 노드와 연결된 다른 노드 탐색
            if not visited[j] and connected:  # 방문하지 않았고, 연결되어 있다면
                dfs(j)

    for idx in range(n):  # 모든 노드를 확인
        if not visited[idx]:  # 방문하지 않은 네트워크 시작점 발견
            dfs(idx)
            result += 1  # 네트워크 수 증가

    return result

def solution_43_BFS2(n, computers):    
    visit = [0 for i in range(n)]
    answer = 0
    def BFS(node):
        que = [node]
        visit[node] = 1
        while que:
            v = que.pop(0)
            for i in range(n):
                if computers[v][i] == 1 and visit[i] == 0:
                    visit[i] = 1
                    que.append(i)
    for i in range(n):
        try:
            if not visit[i]:
              BFS(i)
              answer += 1
        except:
            break
    return answer


def solution_43_DFS(n, computers):
  result = 0 
  visited = [ False for _ in range(n) ]
  
  def dfs(i):
    visited[i] = True
    for j, v in enumerate(computers[i]):
        if visited[j] == False and v == 1:
            dfs(j)

  for i, v in enumerate(computers):
      if visited[i] == False:
          dfs(i)
          result +=1

  return result

def solution_43_BFS(n, computers):
  result = 0 

  visited = [ False for _ in range(n) ]
  def bfs(start):
    q = [start]
    visited[start] = True
    while q:
      value = q.pop(0)
      for i, v in enumerate(computers[value]):
          if visited[i] == False and v == 1:
              visited[i] = True
              q.append(i)
    

  for i, v in enumerate(computers):
      if visited[i] == False:          
          bfs(i)
          result +=1
  print(visited)
  

  return result

N = 3
computers = [
         [1,1,0] # 0
        ,[1,1,0] # 1
        ,[0,0,1] # 2
      ]
print(solution_43_DFS(N, computers)) # 2
print(solution_43_BFS(N, computers)) # 2

# 44 배달 다익스트라 BFS 최단거리 알고리즘
from heapq import heappush, heappop

def solution_44(N, load, K):
  result = 0
  # 간선 연결 인접그래프
  graph = [ []  for _ in range(N + 1) ]
  # 거리 
  distances = [ float("inf") for _ in range(N+1) ]
  
  for a, b, cost in load:
    graph[a].append((cost, b))
    graph[b].append((cost, a))
  
  
  def bfs(start):
    heap = [start]
    distances[start[1]] = start[0]
    while heap:
      curr_cost, node = heappop(heap)
      for next_cost, next_node in graph[node]:
        cost = curr_cost + next_cost
        if distances[next_node] > cost:
          distances[next_node] = cost
          heappush(heap, (cost ,next_node))
  
  bfs((0,1))

  for i, v in enumerate(distances):
    if v <= K:
      result += 1

  return result

N = 5
K = 3 
load = [
         [1,2,1]
        ,[2,3,3]
        ,[5,2,2]
        ,[1,4,2]
        ,[5,3,1]
        ,[5,4,2]
      ]
print(solution_44(N, load, K)) # 

# 45