# 최소 코인
def min_coins(coins, change):
    count = 0
    for coin in coins:
        count += change // coin  # 현재 동전으로 줄 수 있는 개수 추가
        change %= coin  # 남은 거스름돈 갱신
    return count

coins = [500, 100, 50, 10]
change = 1260
print(min_coins(coins, change))  # 6

# 회의실배정
def max_meetings(meetings):
    meetings.sort(key=lambda x: x[1])  # 종료 시간이 빠른 순으로 정렬
    count = 0
    last_end = 0

    for start, end in meetings:
        if start >= last_end:  # 이전 회의가 끝난 후 시작할 수 있다면 선택
            count += 1
            last_end = end  # 끝나는 시간 업데이트

    return count

meetings = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
print(max_meetings(meetings))  # 4

# 배낭
def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)  # 무게 대비 가치가 높은 순 정렬
    total_value = 0

    for weight, value in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += (value / weight) * capacity  # 남은 공간만큼 가치 비율로 추가
            break  # 배낭이 꽉 차면 종료

    return total_value

items = [(6, 30), (3, 14), (4, 16), (2, 9)]  # (무게, 가치)
capacity = 10
print(fractional_knapsack(items, capacity))  # 46.0
