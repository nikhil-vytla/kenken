import numpy
import random


#check to see if there are any other of the same letter in that row
def checkRow(grid, y):
  global a

  for x1 in range(a):
    for x2 in range(a):
      if(x1 == x2):
        continue
      elif(grid[x1][y].num == grid[x2][y].num):
        return False
  return True

#check to see if there are any other of the same letter in that column
def checkColumn(grid, x):
  global a

  for y1 in range(a):
    for y2 in range(a):
      if(y1 == y2):
        continue
      elif(grid[x][y1].num == grid[x][y2].num):
        return False
  return True

def checkGrid(grid):
  for x in range(a):
    if(checkColumn(x) == False):
      return false
  for y in range(a):
    if(checkRow(y) == False):
      return false
  #for Sections in Sections Array
    #checkSections for validity
  return true

#check Sections held in Section array to see if valid
#def checkSection(grid, letter):
  
  

#print grid
def printGrid(fullGrid):
  global a
  for y in range(a):
    print("")
    for x in range(a):
      print(fullGrid[x][y].num, end = ' ')
  print("")




def randomInit(fullGrid:
  global a
  for y in range(a):
    for x in range(a):
      fullGrid[x][y].num = random.randint(1,a)
  return fullGrid




class Section:
  def __init__(self, letter, numEls, arr, ):
    self.letter = letter
    self.numEls = numEls
    self.arr = arr
    

  def getLetter(self):
    return self.letter

  def incEls():
    self.numElse += 1

class Box:
  def __init__(self, letter, xPos, yPos):
    self.letter = letter
    self.xPos = xPos
    self.yPos = yPos
    self.num = 0
    possible = []

  def printBox(self):
    print("Box letter is " + self.letter + " at " + str(self.xPos)
          + ", " + str(self.yPos))

  def constrained(box)
  
    return box.possibleValues



a = int(input())
fullGrid = [[0 for x in range(a)] for y in range(a)]
sections = [0 for x in range(a)]




inputs = []
boxes = []

#Iterate down rows to add Strings of characters to array
y = 0
while(y < a):
  b = str(input())

  
  inputs.append(b)

  #Iteratre through characters in each array and make new Boxs
  x = 0
  while(x < a):
    newBox = Box(b[x], x, y)
    newBox.printBox()
    fullGrid[x][y] = newBox
    x += 1

  y += 1

    
print(a)
print(inputs)
printGrid(randomInit(fullGrid))
print("Is row valid?")
print(checkRow(fullGrid, 0))
print("Is column valid?")
print(checkColumn(fullGrid, 0))

