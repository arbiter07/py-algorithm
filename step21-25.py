# 21 할인 행사
def solution_21(want, number, discount):
  
  dic = {}
  for i, product in enumerate(want):
    dic[product] = number[i]

  
  result = 0
  for i in range(len(discount) - 9):
    temp_dic = dic.copy()
    for j in range(i, i+10):
      if discount[j] in temp_dic:
        temp_dic[discount[j]] -= 1
    isPossible = True
    for key in temp_dic.keys():
      if temp_dic[key] > 0:
        isPossible = False
        break
    if isPossible:
      result += 1 

  return result

want = ["banana", "apple", "rice", "pork" , "pot"]
number = [3,2,2,2,1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution_21(want, number, discount)) # 3