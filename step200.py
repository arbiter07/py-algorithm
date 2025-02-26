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
