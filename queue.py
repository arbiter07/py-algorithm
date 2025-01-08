from collections import deque

q = []

q.append(1)
q.append(2)
q.append(3)
pop = q.pop(0)

dq = deque()
dq.append(1)
dq.append(2)
dq.popleft()