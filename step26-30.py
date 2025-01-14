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