# 36 전화번호 목록
def solution_36(phone_book):
    phone_book.sort()
    for idx in range(len(phone_book) -1):
        before = phone_book[idx]
        after = phone_book[idx + 1]
        if(after.startswith(before)):
            return False
    return True
phone_book = ["119", "97674223", "1195524421"]
print(solution_36(phone_book))  # false

# 37 섬 연결하기
# 1-2-3-4 EX) 4의 부모를 찾을 경우 역순으로 호출하여 1을 세팅함
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# 부모가 다른경우 합침
def union(parent, rank, xroot, yroot):
   
    if rank[xroot] < rank[yroot]:
      parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
      parent[yroot] = xroot
    else:
      parent[yroot] = xroot
      rank[xroot] += 1


def solution_37(n, costs):
    costs.sort(key=lambda x : x[2])
    parent = [i for i in range(n)]
    rank = [0] * n

    # 최소 신장 트리의 총 비용
    min_cost = 0
    # 간선의 개수
    edges = 0 
    
    for edge in costs:
      if edges == n-1:
        break
      # 루트(부모) 검색
      xroot = find(parent, edge[0])
      yroot = find(parent, edge[1])
      # 부모가 다른 경우 합침 (부모가 같은경우에 합치면 사이클이 형성되어버림)
      if xroot != yroot:
        union(parent ,rank, xroot, yroot)
        min_cost += edge[2]
        edges += 1

    return min_cost
n = 4
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
print(solution_37(n, costs))  # 4

# 38 깊이 우선 탐색 순회
def solution_38(graph, start):
    array = [[0 for _ in range(24)] for _ in range(24)]
    visited = set()
    result = []
    for a, b in graph:
        a = ord(a) - 65
        b = ord(b) - 65
        array[a][b] = 1
        array[b][a] = 1
    
    def dfs(graph, start):
        visited.add(start)
        result.append(chr(start + 65))
        for i, obj in enumerate(array[start]):
            if obj and i not in visited:
                dfs(graph, i)
            
    dfs(graph , ord(start) - 65)

    return result

graph = [ ['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']  ]
start = 'A'

print(solution_38(graph, start))

# 39 너비 우선 탐색 조회
def solution_39(graph, start):
  array = [[0 for _ in range(101)] for _ in range(101)]
  result = []
  visited = set()
  for a, b in graph:
    array[a][b] = 1
    array[b][a] = 1
    
  def bfs(graph, q):
    while q:
      node = q.pop(0)
      print(node)
      for idx in range(len(array[node])):
        if idx not in visited and array[node][idx] == 1:
          visited.add(idx)
          result.append(idx)
          q.append(idx) 
  
  q = [start]
  visited.add(start)
  result.append(start)
  bfs(graph, q)

  return result

#graph = [ (1,2), (1,3), (2,4), (2,5), (3,6), (3,7), (4,8), (5,8), (6,9), (7,9) ]
graph = [ (0,1), (1,2), (2,3), (3,4), (4,5), (5,0)]
start = 1

print(solution_39(graph, start)) # 1 2 3 4 5 6 7 8 9 

# 40 다익스트라
import heapq
def solution_40(graph, start):
  distances = { node : float('inf') for node in graph }
  distances[start] = 0 # A 초기화
  q = []
  heapq.heappush(q, [distances[start], start]) # [ 0 , 'A' ]
  paths = {start : [start]} # { 'A' : [ 'A' ] }

  while q:
    curr_distance, curr_node = heapq.heappop(q)
    print(curr_distance, curr_node)
    # 방문처리
    if distances[curr_node] < curr_distance:
      continue
    
    for adjacent_node, weight in graph[curr_node].items():
      distance = curr_distance + weight
      if distance < distances[adjacent_node]:
        distances[adjacent_node] = distance
        paths[adjacent_node] = paths[curr_node] + [adjacent_node]
        heapq.heappush(q, [distance, adjacent_node])
        print(q)
  sorted_paths = {node: paths[node] for node in sorted(paths)}
  print(paths)

  return [distances, sorted_paths]

graph = {
  'A' : {'B' : 9, 'C' : 3},
  'B' : {'A' : 5},
  'C' : {'B' : 1}
}
start = 'A'

print(solution_40(graph, start))

 
