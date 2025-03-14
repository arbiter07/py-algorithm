def bj_2098(N, W):
    INF = float('inf')

    # DP 테이블 초기화: dp[현재 위치][방문 상태] = 최소 비용
    dp = [[INF] * (1 << N) for _ in range(N)]

    # 모든 도시 방문 완료 상태 (비트마스크)
    ALL_VISITED = (1 << N) - 1

    def tsp(city, visited):
        # 모든 도시 방문 완료한 경우, 출발 도시로 복귀 비용 반환
        if visited == ALL_VISITED:
            return W[city][0] if W[city][0] > 0 else INF

        # 이미 계산된 경우 바로 반환
        if dp[city][visited] != INF:
            return dp[city][visited]

        # 다음 방문할 도시 탐색
        for next_city in range(N):
            if visited & (1 << next_city) == 0 and W[city][next_city] > 0:
                dp[city][visited] = min(
                    dp[city][visited],
                    tsp(next_city, visited | (1 << next_city)) + W[city][next_city]
                )

        return dp[city][visited]

    return tsp(0, 1)  # 0번 도시에서 시작, 0번 도시 방문한 상태로 시작

# 예제 입력
N = 4
W = [
    [0, 10, 15, 20],
    [5, 0, 9, 10],
    [6, 13, 0, 12],
    [8, 8, 9, 0]
]

# 함수 호출 및 출력
print(bj_2098(N, W))  # 35

from collections import deque

def tomato_3d(M, N, H, box):
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    queue = deque()
    total_tomatoes, ripe_tomatoes = 0, 0

    # 초기 상태 확인 (익은 토마토 찾기)
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[h][n][m] == 1:
                    queue.append((h, n, m, 0))  # (층, 행, 열, 날짜)
                    ripe_tomatoes += 1
                if box[h][n][m] != -1:
                    total_tomatoes += 1

    max_days = 0

    # BFS 탐색
    while queue:
        h, n, m, days = queue.popleft()
        max_days = max(max_days, days)

        for dh, dn, dm in directions:
            nh, nn, nm = h + dh, n + dn, m + dn
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and box[nh][nn][nm] == 0:
                box[nh][nn][nm] = 1
                queue.append((nh, nn, nm, days + 1))
                ripe_tomatoes += 1

    return max_days if ripe_tomatoes == total_tomatoes else -1

# 예제 실행
M, N, H = 5, 3, 2
box = [
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
]
print(tomato_3d(M, N, H, box))  # 예상 출력: 4

def count_ways(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    dp = [0] * (n + 1)
    dp[1], dp[2], dp[3] = 1, 2, 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    return dp[n]

# 예제 실행
print(count_ways(4))  # 7

def bj_11053(n: int, arr: list) -> int:
    dp = [1] * n  # 모든 dp[i]를 1로 초기화

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:  # 증가하는 경우
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # 가장 긴 부분 수열의 길이 반환

# 예제 실행
print(bj_11053(6, [10, 20, 10, 30, 20, 50]))  # 4

def bj_14503(N, M, r, c, d, room):
    # 방향 벡터 (북, 동, 남, 서)
    dx = [-1, 0, 1, 0]  # row 이동
    dy = [0, 1, 0, -1]  # col 이동

    cleaned = 0  # 청소한 칸 개수

    while True:
        # 현재 위치 청소
        if room[r][c] == 0:
            room[r][c] = 2  # 청소 완료
            cleaned += 1

        # 네 방향 모두 확인
        found = False
        for _ in range(4):
            d = (d - 1) % 4  # 왼쪽 방향으로 회전
            nx, ny = r + dx[d], c + dy[d]

            if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
                r, c = nx, ny  # 이동
                found = True
                break

        # 네 방향 모두 청소되어 있거나 벽인 경우
        if not found:
            back_dir = (d + 2) % 4  # 뒤쪽 방향
            br, bc = r + dx[back_dir], c + dy[back_dir]

            if room[br][bc] == 1:  # 뒤쪽이 벽이면 멈춤
                break
            else:
                r, c = br, bc  # 후진

    return cleaned


N = 3
M = 3
r = 1
c = 1
d = 0
room = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print(bj_14503(N, M, r, c, d, room))  # 출력: 1

def bj_17144(R, C, T, room):
    from copy import deepcopy

    # 상, 하, 좌, 우 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 공기청정기 위치 찾기
    air_cleaner = []
    for i in range(R):
        if room[i][0] == -1:
            air_cleaner.append(i)

    # 미세먼지 확산
    def spread():
        new_room = deepcopy(room)

        for x in range(R):
            for y in range(C):
                if room[x][y] > 0:
                    spread_amount = room[x][y] // 5
                    spread_count = 0

                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:
                            new_room[nx][ny] += spread_amount
                            spread_count += 1

                    new_room[x][y] -= spread_amount * spread_count

        return new_room

    # 공기청정기 작동 (위쪽 / 아래쪽)
    def operate_air_cleaner():
        # 위쪽 공기청정기 (반시계 방향 순환)
        upper = air_cleaner[0]
        for i in range(upper - 1, 0, -1):
            room[i][0] = room[i - 1][0]
        for i in range(C - 1):
            room[0][i] = room[0][i + 1]
        for i in range(upper):
            room[i][C - 1] = room[i + 1][C - 1]
        for i in range(C - 1, 0, -1):
            room[upper][i] = room[upper][i - 1]
        room[upper][1] = 0

        # 아래쪽 공기청정기 (시계 방향 순환)
        lower = air_cleaner[1]
        for i in range(lower + 1, R - 1):
            room[i][0] = room[i + 1][0]
        for i in range(C - 1):
            room[R - 1][i] = room[R - 1][i + 1]
        for i in range(R - 1, lower, -1):
            room[i][C - 1] = room[i - 1][C - 1]
        for i in range(C - 1, 0, -1):
            room[lower][i] = room[lower][i - 1]
        room[lower][1] = 0

    # T초 동안 시뮬레이션 진행
    for _ in range(T):
        room = spread()
        operate_air_cleaner()

    # 미세먼지 총량 계산
    return sum(sum(row) for row in room if row[0] != -1)


# ✅ 예제 실행
R = 7
C = 8
T = 1
room = [
    [0, 0, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 3, 0],
    [-1, 0, 5, 0, 0, 0, 0, 0],
    [-1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 15, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

print(bj_17144(R, C, T, room))  # 결과 출력

def robot_vacuum(N, M, r, c, d, room):
    # 0: 북, 1: 동, 2: 남, 3: 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 청소한 영역 카운트
    cleaned_count = 0

    while True:
        # 1. 현재 위치 청소
        if room[r][c] == 0:
            room[r][c] = 2  # 청소 완료
            cleaned_count += 1

        # 2. 네 방향 탐색
        found_cleanable = False
        for _ in range(4):
            d = (d - 1) % 4  # 반시계 방향 회전
            nx, ny = r + dx[d], c + dy[d]

            if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
                # 청소되지 않은 곳이 있다면 이동
                r, c = nx, ny
                found_cleanable = True
                break

        if not found_cleanable:
            # 후진
            back_x, back_y = r - dx[d], c - dy[d]
            if room[back_x][back_y] == 1:  # 벽이면 종료
                break
            r, c = back_x, back_y  # 후진

    return cleaned_count


# 입력 예제
N, M = 3, 3
r, c, d = 1, 1, 0
room = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

# 실행
print(robot_vacuum(N, M, r, c, d, room))  # 출력: 1

from collections import deque

def bj_2178(n, m, maze):
    dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dy = [0, 0, -1, 1]

    queue = deque([(0, 0)])  # 시작점 (0,0)
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):  # 네 방향 탐색
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1  # 거리 갱신
                queue.append((nx, ny))

    return maze[n-1][m-1]  # 도착점 (N-1, M-1)의 값이 최소 이동 거리

# 예제 실행
n, m = 4, 6
maze = [
    [1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1]
]

print(bj_2178(n, m, maze))  # 15

def bj_15649(n, m):
    result = []
    visited = [False] * (n + 1)

    def backtrack(sequence):
        if len(sequence) == m:
            result.append(" ".join(map(str, sequence)))
            return
        
        for num in range(1, n + 1):
            if not visited[num]:
                visited[num] = True
                backtrack(sequence + [num])
                visited[num] = False

    backtrack([])
    return "\n".join(result)

# 예제 실행
n, m = 3, 2
print(bj_15649(n, m))

def bj_14888(n, numbers, operators):
    max_value = -float('inf')
    min_value = float('inf')

    def backtrack(index, current_value):
        nonlocal max_value, min_value
        if index == n:
            max_value = max(max_value, current_value)
            min_value = min(min_value, current_value)
            return
        
        for i in range(4):
            if operators[i] > 0:
                operators[i] -= 1
                next_value = calculate(current_value, numbers[index], i)
                backtrack(index + 1, next_value)
                operators[i] += 1  # 백트래킹 (원상복구)

    def calculate(a, b, operator_type):
        if operator_type == 0:  # 덧셈
            return a + b
        elif operator_type == 1:  # 뺄셈
            return a - b
        elif operator_type == 2:  # 곱셈
            return a * b
        else:  # 나눗셈 (음수 나눗셈 처리)
            return int(a / b) if a >= 0 else -(-a // b)

    backtrack(1, numbers[0])
    return max_value, min_value

# 예제 실행
n = 2
numbers = [5, 6]
operators = [0, 0, 1, 0]  # 덧셈 0개, 뺄셈 0개, 곱셈 1개, 나눗셈 0개
print(bj_14888(n, numbers, operators))  # (30, 30)
