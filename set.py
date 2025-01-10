# 중복 제거
numbers = [1, 2, 3, 4, 4, 5, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # 출력: {1, 2, 3, 4, 5}

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# 합집합
print(set_a | set_b)  # 출력: {1, 2, 3, 4, 5, 6}
print(set_a.union(set_b))  # 동일한 결과

# 교집합
print(set_a & set_b)  # 출력: {3, 4}
print(set_a.intersection(set_b))  # 동일한 결과

# 차집합
print(set_a - set_b)  # 출력: {1, 2}
print(set_a.difference(set_b))  # 동일한 결과

# 대칭 차집합
print(set_a ^ set_b)  # 출력: {1, 2, 5, 6}
print(set_a.symmetric_difference(set_b))  # 동일한 결과

set_c = {1, 2, 3, 4}
print(3 in set_c)  # 출력: True
print(5 in set_c)  # 출력: False

set_d = {1, 2, 3}
set_d.add(4)  # {1, 2, 3, 4}
set_d.remove(3)  # {1, 2, 4}
set_d.discard(2)  # {1, 4}
set_d.clear()  # {}