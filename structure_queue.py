import queue

q = queue.Queue()

# 항목 추가
q.put(1)
q.put(2)
q.put(3)

# 항목 꺼내기
print(q.get())  # 출력: 1
print(q.get())  # 출력: 2
print(q.get())  # 출력: 3

from collections import deque

d = deque()

# 오른쪽에 요소 추가
d.append(1)
d.append(2)

# 왼쪽에 요소 추가
d.appendleft(0)

# 오른쪽에서 요소 제거
print(d.pop())  # 출력: 2

# 왼쪽에서 요소 제거
print(d.popleft())  # 출력: 0

# 남은 요소들 출력
print(d)  # 출력: deque([1])