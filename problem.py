def dp_xy():
  # 테스트 데이터 (입력 없이 실행 가능)
  n = 3  # 행렬 개수
  matrices = [(5, 3), (3, 2), (2, 6)]  # 행렬 크기 리스트

  # DP 테이블 초기화
  dp = [[0] * n for _ in range(n)]

  # DP 계산 (부분 행렬의 길이 2 이상)
  for length in range(2, n + 1):  # 부분 길이
      for i in range(n - length + 1):
          j = i + length - 1
          dp[i][j] = float('inf')  # 최소값을 찾기 위해 초기화
          for k in range(i, j):
              cost = dp[i][k] + dp[k+1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]
              dp[i][j] = min(dp[i][j], cost)

  return dp[0][n-1]

# 최소 연산 횟수 출력
print(dp_xy())  # 결과: 90
