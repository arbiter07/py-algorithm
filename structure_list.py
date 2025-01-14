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

############ 

# 빈 리스트
empty_list = []

# 초기 요소로 리스트 생성
numbers = [1, 2, 3, 4]

# 요소 접근
print(numbers[0])  # 출력: 1

# 요소 수정
numbers[1] = 5
print(numbers)  # 출력: [1, 5, 3, 4]

numbers.append(6)  # [1, 5, 3, 4, 6]
numbers.insert(1, 2)  # [1, 2, 5, 3, 4, 6]
numbers.extend([7, 8])  # [1, 2, 5, 3, 4, 6, 7, 8]

numbers.pop()  # [1, 2, 5, 3, 4, 6, 7]
numbers.remove(5)  # [1, 2, 3, 4, 6, 7]
numbers.clear()  # []

numbers = [3, 1, 4, 2]
numbers.sort()  # [1, 2, 3, 4]
numbers.reverse()  # [4, 3, 2, 1]

# 1부터 10까지의 제곱 리스트 생성
squares = [x**2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]