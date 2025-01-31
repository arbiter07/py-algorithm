
# 61
# 62 배열 회전하기
def solution_62(arr : list , n : int):

  N = len(arr)
  # i,j == j , (N-1)-i 

  rotate_arr = [[0 for _ in range(N)] for _ in range(N)]

  for _ in range(n):
    for y in range(N):
      for x in range(N):
        rotate_arr[x][N-1-y] = arr[y][x]
        print(y,x)
      
  return rotate_arr

arr = [ 
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12],
  [13,14,15,16],
]
n = 1
print(solution_62(arr, n))

# 63
# 64
# 65 이진 변환
def solution_65(s : str):
  result_zero = 0
  result_count = 0

  while s != "1":
    result_count += 1
    result_zero += s.count("0")
    len_remove_zero = len(s.replace("0", ""))
    s = bin(len_remove_zero)[2:]
    
  return [result_count, result_zero]

s = "110010101001"
print(solution_65(s))