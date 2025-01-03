# 배열 초기화
arr = [i for i in range(6)] # 0,1,2,3,4,5
print('초기화 : ' , arr)

# 배열 삽입
arr.append(6)
print('append : ' , arr)

# 배열 원하는 위치에 삽입
arr.insert(1, 5)
print('insert : ' , arr)

# 배열 원하는 위치 삭제
arr.pop(1)
print('pop : ' , arr)

# 배열 삭제 remove 매개변수를 값으로 가지는 위치 삭제 (첫번째)
arr.append(6)
arr.remove(6)
print('remove : ' , arr)

# 리스트 컴프리헨션 모든 데이터에 특정 연산 적용
# 새로운 배열을 반환한다.
comprehension = [num**2 for num in arr]
print('comprehension : ' , comprehension)

# 리스트 길이 
print('arr len : ' , len(arr))
print('arr.index(1) : ' , arr.index(1))
print('arr.count(1) : ' , arr.count(1))

# 정렬 값을 반환하지 않고 내부적으로 수행
arr.sort()
print('sort arr : ' , arr)

arr.sort(reverse=True)
print('reverse arr : ' , arr)

# 원본은 그대로 두면서 새로운 배열 생성 
sorted_list = list(sorted(arr))
print('sorted_list : ' , sorted_list)

# 중복값 제거 
unique_list = list(set(arr))

