# 30 미로 탈출
from collections import deque

def is_valid_move(ny, nx, n, m , maps):
    return 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X"

def bfs(start_y, start_x, end_char, n, m, maps):
    visited = [[False for _ in range(m)] for _ in range(n)]
    time = 0
    q = deque([(start_y, start_x, time)])
    print(q)
    visited[start_y][start_x] = True

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        y, x, time = q.popleft()

        if maps[y][x] == end_char:
            return y, x, time

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            print(ny, nx, time)
            if is_valid_move(ny, nx, n, m, maps) and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, time + 1))

    return -1, -1, -1

def solution_30(maps):
    n, m = len(maps), len(maps[0])

    # 시작점에서 레버까지의 최단 거리
    start_y, start_x = [(i, j) for i in range(n) for j in range(m) if maps[i][j] == "S"][0]
    lever_y, lever_x, time_to_lever = bfs(start_y, start_x, "L", n, m, maps)

    if time_to_lever == -1:
        return -1

    # 레버에서 도착점까지의 최단 거리
    _, _, time_to_end = bfs(lever_y, lever_x, "E", n, m, maps)

    if time_to_end == -1:
        return -1

    return time_to_lever + time_to_end

maps = [
    "LOOOO",
    "XXXXO",
    "OOSOO",
    "OXXXX",
    "OOOOE"
]
print(solution_30(maps))  # 16
