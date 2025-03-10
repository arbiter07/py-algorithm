def count_subsequences(n, s, arr):
    count = 0

    def backtrack(index, total):
        nonlocal count
        if index >= n:
            return
        total += arr[index]

        # 합이 S가 되는 경우 카운트 증가
        if total == s:
            count += 1

        # 현재 원소를 포함하는 경우
        backtrack(index + 1, total)

        # 현재 원소를 포함하지 않는 경우
        backtrack(index + 1, total - arr[index])

    backtrack(0, 0)
    return count

# 초기값 지정
n = 5
s = 0
arr = [-7, -3, -2, 5, 8]

# 함수 실행 및 결과 출력
result = count_subsequences(n, s, arr)
print(result)

from collections import deque

def bj_16953(A, B):
    queue = deque([(A, 1)])  # (현재 값, 연산 횟수)
    
    while queue:
        current, count = queue.popleft()
        
        if current == B:
            return count  # B에 도달하면 연산 횟수 반환
        
        # 2배 연산 수행
        if current * 2 <= B:
            queue.append((current * 2, count + 1))
        
        # 오른쪽에 1 추가 연산 수행
        if current * 10 + 1 <= B:
            queue.append((current * 10 + 1, count + 1))
    
    return -1  # B를 만들 수 없는 경우

# 예제 실행
print(bj_16953(2, 162))  # ➝ 5
print(bj_16953(4, 42))   # ➝ -1
