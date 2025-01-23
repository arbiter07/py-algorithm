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

  