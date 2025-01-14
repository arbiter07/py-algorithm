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

# 23 베스트 앨범
def solution_23(genres, plays):

  result = []
  genres_dict = {}
  play_dict = {}
  
  for i in range(len(genres)):
    genre = genres[i]
    play = plays[i]
    if genre not in genres_dict:
      genres_dict[genre] = []
      play_dict[genre] = 0
    genres_dict[genre].append((i,play))
    play_dict[genre] += play

  sorted_genres = sorted(play_dict.items(), key=lambda x : x[1], reverse=True)
  print(sorted_genres)

  for genre, _ in sorted_genres:
    sorted_songs = sorted(genres_dict[genre], key=lambda x : (-x[1], x[0]))
    #result.extend([idx for idx, _ in sorted_songs[:2]])
    result.extend(list(map(lambda x: x[0], sorted_songs[:2])))
  

  return result

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution_23(genres, plays)) # [4,1,3,0]

# 24 신고 결과 받기
class User:
    def __init__(self, id):
        self.name = id
        self.call_id = set()
        self.report_cnt = 0

    def print(self):
        print('name:', self.name)
        print('call_id:', self.call_id)
        print('report_cnt:', self.report_cnt)
        print()

def solution_24(id_list, report, k):
  result = []
  userDic = {}

  for id in id_list:
    userDic[id] = (User(id)) 

  for r in report:
    r_split = r.split(" ")
    _from = r_split[0]
    _to = r_split[1]
    if _to not in userDic[_from].call_id:
      userDic[_to].report_cnt += 1 
      userDic[_from].call_id.add(_to)
  
  for user in userDic:
    reportResult = 0
    for user in userDic[user].call_id:
       if userDic[user].report_cnt >= k:
          reportResult += 1
    result.append(reportResult)
  return result

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution_24(id_list, report, k)) # 2 1 1 0

# 25 메뉴 리뉴얼
from itertools import combinations
from collections import Counter
def solution_25(orders, course):
  result = []

  for c in course:
    menu = []
    for order in orders:
      comb = combinations( sorted(order) , c )
      menu += comb
    counter = Counter(menu)
    if ( len(counter) != 0 and max(counter.values()) != 1 ):
      for m , cnt in counter.items():
        if cnt == max(counter.values()):
          result.append("".join(m))
  
  return result

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

print(solution_25(orders, course)) # ['AC', 'CDE', 'BCFG', 'ACDE']