# 7 방문길이
keyset = { 'U' : (0,-1), 'D' : (0,1), 'L' : (-1,0), 'R' : (1,0) }
x,y = 5,5

def solution_7(dirs):
  ans = set()
  global x,y
  for dir in dirs:
    nx = x + keyset[dir][0]
    ny = y + keyset[dir][1]
    if not checkLocation(nx,ny):
      continue
    
    ans.add((x,y,nx,ny))
    ans.add((nx,ny,x,y))
    x, y = nx, ny

  return len(ans)/2

def checkLocation(nx,ny):
  return 0 <= nx < 11 and 0 <= ny < 11

# dirs = 'ULURRDLLU'
dirs = 'ULURRDLLU'
print(solution_7(dirs))