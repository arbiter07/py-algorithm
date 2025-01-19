# 31
# 32
# 33 유니온 파인드 연습문제
def solution_33(k, operations):

    _list = [ x for x in range(k) ]

    for op in operations:
        if op[0] == 'u':
            union(_list, op[1], op[2])
        else:
            find(_list, op[1])
    print(_list)
    return len(set(_list))

def union(list , op1, op2):
    root1 = find(list, op1)
    root2 = find(list, op2)
    
    list[root2] = root1
    
def find(list, op):
    if list[op] == op:
        return op
    list[op] == find(list, list[op])
    return list[op]

k = 4
operations = [ ['u' , 0 , 1], ['u' , 2 , 3], ['f' , 0] ] 
print(solution_33(k, operations))  # 1

# 34 폰켓몬
def solution_34(nums):
  max_num = len(nums) // 2 
  num_set = set(nums)
  
  return min(max_num, len(num_set))
nums = [3,1,2,3]
print(solution_34(nums))  # 2

# 35 영어 끝말잇기
def solution_35(n, words):
  word_set = set()
  pre_char = words[0][0]
  for idx, word in enumerate(words):
    if word[0] != pre_char or word in word_set:
        return [( idx % n ) + 1, idx // n + 1]
    word_set.add(word)
    pre_char = word[-1]
    
    
  return [0,0]
n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution_35(n, words))  # 2