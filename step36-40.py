# 36 전화번호 목록
def solution_36(phone_book):
    phone_book.sort()
    for idx in range(len(phone_book) -1):
        before = phone_book[idx]
        after = phone_book[idx + 1]
        if(after.startswith(before)):
            return False
    return True
phone_book = ["119", "97674223", "1195524421"]
print(solution_36(phone_book))  # false

# 37 섬 연결하기
# 1-2-3-4 EX) 4의 부모를 찾을 경우 역순으로 호출하여 1을 세팅함
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# 부모가 다른경우 합침
def union(parent, rank, xroot, yroot):
   
    if rank[xroot] < rank[yroot]:
      parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
      parent[yroot] = xroot
    else:
      parent[yroot] = xroot
      rank[xroot] += 1


def solution_37(n, costs):
    costs.sort(key=lambda x : x[2])
    parent = [i for i in range(n)]
    rank = [0] * n

    # 최소 신장 트리의 총 비용
    min_cost = 0
    # 간선의 개수
    edges = 0 
    
    for edge in costs:
      if edges == n-1:
        break
      # 루트(부모) 검색
      xroot = find(parent, edge[0])
      yroot = find(parent, edge[1])
      # 부모가 다른 경우 합침 (부모가 같은경우에 합치면 사이클이 형성되어버림)
      if xroot != yroot:
        union(parent ,rank, xroot, yroot)
        min_cost += edge[2]
        edges += 1

    return min_cost
n = 4
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
print(solution_37(n, costs))  # 4