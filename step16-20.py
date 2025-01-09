# 16 기능 개발
def solution_16(progresses, speeds):
  ret = []
  execute_days = [] 
  # 7 3 9
  
  for i, v in enumerate(progresses):
    day = 0
    while v < 100:
      v += speeds[i]
      day+=1
    execute_days.append(day)

  while len(execute_days) > 0:
    pop = execute_days.pop(0)
    group = 1
    while len(execute_days) > 0:
      next = execute_days[0]
      if pop >= next:
        execute_days.pop(0)
        group +=1
      else: 
        break
    ret.append(group)

  return ret

# progresses = [93,30,55]
# speeds = [1,30,5]

progresses = [95,90,99,99,80,99]
speeds = [1,1,1,1,1,1]
print(solution_16(progresses, speeds))

# 17 카드뭉치
def solution_17(cards1, cards2, goal):

  for _ in range(len(goal)):
    c = goal[0]
    if cards1 and c==cards1[0]:
      cards1.pop(0)
      goal.pop(0)
    elif cards2 and c==cards2[0]:
      cards2.pop(0)
      goal.pop(0)
    else:
      break
  print(goal)
  return "Yes" if not goal else "No"

cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
print(solution_17(cards1, cards2, goal))