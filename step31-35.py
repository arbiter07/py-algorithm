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
