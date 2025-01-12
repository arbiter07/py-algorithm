# 21 할인행사
def solution_21(want, number, discount):
    dic = {}
    for i, product in enumerate(want):
        dic[product] = number[i]
    
    result = 0
    
    for i in range(len(discount) - 9):  # 10일 기간이기 때문에 범위 수정
        temp_dic = dic.copy()  # 매번 초기화를 위해 dic 복사본 사용
        isPossible = True
        
        for j in range(i, i + 10):
            if discount[j] in temp_dic:
                temp_dic[discount[j]] -= 1
                if temp_dic[discount[j]] < 0:
                    isPossible = False
                    break
        
        if isPossible and all(value == 0 for value in temp_dic.values()):
            result += 1
    
    return result

# 테스트 케이스
want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution_21(want, number, discount))  # 출력: 3

# 22 오픈채팅방
def solution_22(record):
  dic = {}

  # 마지막 이름
  for line in record:
    cmd = line.split(" ")
    if cmd[0] != 'Leave':
      dic[cmd[1]] = cmd[2]

  result = []
  for line in record:
    cmd = line.split(" ")
    action = cmd[0]
    nick = dic[cmd[1]]
    if action == 'Enter':
      result.append('%s님이 들어왔습니다.' %nick)
    elif action == 'Leave':
      result.append('%s님이 나갔습니다.' %nick)

  return result

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution_22(record))