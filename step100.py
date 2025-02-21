def radar_directions(N, coord1, coord2):
    directions = {
        "E": (0, 1),
        "W": (0, -1),
        "S": (1, 0),
        "N": (-1, 0),
        "NE": (-1, 1),
        "NW": (-1, -1),
        "SE": (1, 1),
        "SW": (1, -1),
    }
    
    y1, x1 = coord1
    y2, x2 = coord2
    result = []

    for direction, (dy, dx) in directions.items():
        # Check if (y1, x1) can move to (y2, x2) in the same direction
        if (y2 - y1) * dx == (x2 - x1) * dy:
            # Ensure both are within the same valid range
            if 1 <= y1 + dy * abs(x2 - x1) <= N and 1 <= x1 + dx * abs(x2 - x1) <= N:
                result.append(direction)

    return result if result else ["None"]

# Example Test Case
N = 5
coord1 = (3, 2)
coord2 = (3, 5)
print(radar_directions(N, coord1, coord2))  # Output: ['E']

N = 5
coord1 = (2, 2)
coord2 = (4, 4)
print(radar_directions(N, coord1, coord2))  # Output: ['SE']

def possible_directions(N, start, end):
    directions = {
        "E": (0, 1), "W": (0, -1),
        "S": (1, 0), "N": (-1, 0),
        "NE": (-1, 1), "NW": (-1, -1),
        "SE": (1, 1), "SW": (1, -1),
    }

    sy, sx = start
    ey, ex = end
    result = []

    for direction, (dy, dx) in directions.items():
        # 방향을 유지하며 이동 가능 여부 확인
        if (ey - sy) * dx == (ex - sx) * dy:
            # 이동 과정에서 격자를 벗어나지 않는지 확인
            steps = max(abs(ey - sy), abs(ex - sx))
            if 1 <= sy + dy * steps <= N and 1 <= sx + dx * steps <= N:
                result.append(direction)

    return result if result else ["None"]

# 테스트
N = 5
print(possible_directions(N, (3, 2), (3, 5)))  # ['E']
print(possible_directions(N, (2, 2), (4, 4)))  # ['SE']
print(possible_directions(N, (1, 1), (5, 1)))  # ['S']
print(possible_directions(N, (3, 3), (1, 5)))  # ['NE']
print(possible_directions(N, (2, 2), (3, 4)))  # ['None']


from collections import deque

def is_one_letter_diff(word1, word2):
    """두 단어가 한 글자만 다른지 확인하는 함수"""
    diff_count = sum([1 for a, b in zip(word1, word2) if a != b])
    return diff_count == 1

def bfs(begin, target, words):
    if target not in words:
        return 0  # target이 words 리스트에 없으면 변환 불가
    
    queue = deque([(begin, 0)])  # (현재 단어, 변환 횟수)
    visited = set()  # 방문한 단어 저장

    while queue:
        current, steps = queue.popleft()
        
        if current == target:
            return steps  # 목표 단어에 도달하면 변환 횟수 반환
        
        for word in words:
            if word not in visited and is_one_letter_diff(current, word):
                visited.add(word)
                queue.append((word, steps + 1))  # 변환 횟수 증가

    return 0  # 변환 불가능할 경우

def wordChange(begin, target, words):
    return bfs(begin, target, words)

# 예제 실행
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(wordChange(begin, target, words))  # 출력: 4


import heapq
def heapqSolution(operations):
    min_heap = []
    max_heap = []
    exist = {}

    for op in operations:
        if op[0] == "I":  # 삽입
            num = int(op[2:])
            heapq.heappush(min_heap, num)  
            heapq.heappush(max_heap, -num)
            exist[num] = exist.get(num, 0) + 1  

        elif op == "D 1":  # 최댓값 삭제
            while max_heap:
                max_val = -heapq.heappop(max_heap)
                if exist.get(max_val, 0) > 0:
                    exist[max_val] -= 1
                    break  

        elif op == "D -1":  # 최솟값 삭제
            while min_heap:
                min_val = heapq.heappop(min_heap)
                if exist.get(min_val, 0) > 0:
                    exist[min_val] -= 1
                    break  

    # 남아 있는 값 찾기
    valid_numbers = [k for k, v in exist.items() if v > 0]
    return [max(valid_numbers), min(valid_numbers)] if valid_numbers else [0, 0]


from collections import deque

def farDistanceBFS(n, edge):
    # 그래프 초기화
    graph = {i: [] for i in range(1, n + 1)}
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # BFS를 위한 큐
    queue = deque([1])  # 1번 노드에서 시작
    distances = {1: 0}  # 시작점의 거리 0

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in distances:  # 방문하지 않은 노드라면
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    # 가장 먼 거리 찾기
    max_distance = max(distances.values())
    return sum(1 for d in distances.values() if d == max_distance)

# 테스트
print(farDistanceBFS(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))  # 출력: 3

import heapq

def heapq_solution(operations):
    min_heap = []
    max_heap = []
    visited = {}

    for op in operations:
        cmd, num = op.split()
        num = int(num)

        if cmd == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            visited[num] = visited.get(num, 0) + 1
        elif cmd == "D":
            if num == 1:
                while max_heap and visited.get(-max_heap[0], 0) == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    value = -heapq.heappop(max_heap)
                    visited[value] -= 1
            else:
                while min_heap and visited.get(min_heap[0], 0) == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    value = heapq.heappop(min_heap)
                    visited[value] -= 1

    while min_heap and visited.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)
    while max_heap and visited.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        return [-max_heap[0], min_heap[0]]
    return [0, 0]

# 테스트 실행
operations = ["I 16", "I -5643", "D -1", "D 1", "D 1"]
print(heapq_solution(operations))  # [0, 0]

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


def LIS():
    # 테스트 데이터 (입력 없이 실행 가능)
    arr = [10, 20, 10, 30, 20, 50]  # 주어진 수열
    n = len(arr)

    # DP 테이블 초기화
    dp = [1] * n

    # LIS 계산
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:  # 증가하는 수열인지 확인
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # 가장 긴 증가하는 부분 수열의 길이

print(LIS())  # 출력: 4

from collections import deque

def bj_13549():
    N, K = 5, 17  # 예제 입력

    MAX = 100000
    visited = [-1] * (MAX + 1)
    queue = deque([N])
    visited[N] = 0

    while queue:
        x = queue.popleft()

        if x == K:
            return visited[x]  # 최소 시간 반환

        for nx in [x * 2, x - 1, x + 1]:
            if 0 <= nx <= MAX and visited[nx] == -1:
                if nx == x * 2:  # 순간이동 (0초)
                    queue.appendleft(nx)
                    visited[nx] = visited[x]
                else:  # +1 또는 -1 (1초)
                    queue.append(nx)
                    visited[nx] = visited[x] + 1

print(bj_13549())  # 2
