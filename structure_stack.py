# 스택 기본구조 
# 파이썬은 리스트를 활용하여 append와 pop 내장함수를 사용하기 때문에 구현을 하지 않아도됨
stack = []
max_size = 10

def isFull(stack):
  return len(stack) == max_size

def isEmpty(stack):
  return len(stack) == 0

def push(stack, item):
  if isFull(stack):
    print('스택이 가득 찼습니다.')
  else:
    stack.append(item)
    print('데이터가 추가되었습니다.')

def pop(stack):
  if isEmpty(stack):
    print('스택이 비어있습니다')
    return None
  else:
    return stack.pop()