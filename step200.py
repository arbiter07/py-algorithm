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
