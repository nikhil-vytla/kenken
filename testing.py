a = 6
fullGrid = [[0 for x in range(a)] for y in range(a)]


def checkColumn(grid, xPos, yPos, num):
  global a

  for y in range(a):
    if(y == yPos):
      continue
    elif(fullGrid[xPos][y] == num):
      return False
  return True



print(checkColumn(fullGrid, 2, 3, 0))
