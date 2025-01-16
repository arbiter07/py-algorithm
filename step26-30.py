# 26 트리 순회
def preorder(nodes, idx):
  
  if len(nodes) > idx:
    ret = str(nodes[idx]) + " "
    ret += preorder(nodes, idx * 2 + 1)
    ret += preorder(nodes, idx * 2 + 2)
    return ret
  else:
    return ""

def inorder(nodes, idx):
    if len(nodes) > idx:
        ret = inorder(nodes, idx * 2 + 1)
        ret += str(nodes[idx]) + " "
        ret += inorder(nodes, idx * 2 + 2)
        return ret
    else:
        return ""

def postorder(nodes, idx):
    if len(nodes) > idx:
        ret = postorder(nodes, idx * 2 + 1)
        ret += postorder(nodes, idx * 2 + 2)
        ret += str(nodes[idx]) + " "
        return ret
    else:
        return ""

def solution_26(nodes):
  result = [
    preorder(nodes, 0).strip(),
    inorder(nodes, 0).strip(),
    postorder(nodes, 0).strip(),
  ]

  return result

nodes = [1,2,3,4,5,6,7]
print(solution_26(nodes)) 

# 27 이진 탐색 트리 구현
class Node:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key

class BST:
  def __init__(self):
    self.root = None
  
  def insert(self, key):
    if not self.root:
      self.root = Node(key)
    else:
      curr = self.root
      while True:
        if key < curr.val:
          if curr.left:
            curr = curr.left
          else:
            curr.left = Node(key)
            break
        else:
          if curr.right:
            curr = curr.right
          else:
            curr.right = Node(key)
            break
  
  def search(self, key):
    curr = self.root

    while curr and curr.val != key:
      if key < curr.val:
        curr = curr.left
      else:
        curr = curr.right
    return curr

def solution_27(lst, search_lst):
  bst = BST()
  
  result = [
  ]
  for key in lst:
    bst.insert(key)

  for search_key in search_lst:
    if bst.search(search_key):
      result.append(True)
    else:
      result.append(False)


  return result

lst = [5,3,8,4,2,1,7,10]
search_lst = [1,2,5,6]
print(solution_27(lst, search_lst)) 

# 28 예상 대진표
def solution_28(N, A, B):
  result = 0

  while A != B:
    A = (A+1) // 2
    B = (B+1) // 2
    result += 1 
  
  return result

N = 8
A = 4
B = 7
print(solution_28(N, A, B)) # 3

# 29 다단계 칫솔 판매
def solution_29(enroll, referral, seller, amount):
  result = []

  ref_dic = {}
  total_dic = {}

  # 추천인 // 합계 등록
  for i in range(len(enroll)):
    key = enroll[i]
    val = referral[i]
    ref_dic[key] = val
    total_dic[key] = 0
  
  for i in range(len(seller)):
    curr_name = seller[i]
    money = amount[i] * 100

    while curr_name != '-' and money > 0:
      print(curr_name)
      parent = ref_dic[curr_name]
      total_dic[curr_name] += money - money // 10
      curr_name = parent
      money = money // 10

  return [total_dic[name] for name in enroll]

# 조직 구성원
enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
# 추천인
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution_29(enroll, referral, seller, amount))

# 30 미로 탈출
from collections import deque

def is_valid_move(ny, nx, n, m , maps):
    return 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X"

def bfs(start_y, start_x, end_char, n, m, maps):
    visited = [[False for _ in range(m)] for _ in range(n)]
    time = 0
    q = deque([(start_y, start_x, time)])
    print(q)
    visited[start_y][start_x] = True

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        y, x, time = q.popleft()

        if maps[y][x] == end_char:
            return y, x, time

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            print(ny, nx, time)
            if is_valid_move(ny, nx, n, m, maps) and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, time + 1))

    return -1, -1, -1

def solution_30(maps):
    n, m = len(maps), len(maps[0])

    # 시작점에서 레버까지의 최단 거리
    start_y, start_x = [(i, j) for i in range(n) for j in range(m) if maps[i][j] == "S"][0]
    lever_y, lever_x, time_to_lever = bfs(start_y, start_x, "L", n, m, maps)

    if time_to_lever == -1:
        return -1

    # 레버에서 도착점까지의 최단 거리
    _, _, time_to_end = bfs(lever_y, lever_x, "E", n, m, maps)

    if time_to_end == -1:
        return -1

    return time_to_lever + time_to_end

maps = [
    "LOOOO",
    "XXXXO",
    "OOSOO",
    "OXXXX",
    "OOOOE"
]
print(solution_30(maps))  # 24

