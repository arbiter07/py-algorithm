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
