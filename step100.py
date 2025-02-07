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
