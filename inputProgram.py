import numpy
import random


#check to see if there are any other of the same letter in that row
def checkRow(box):
  global fullGrid
  global a

  for x in range(a):
    if(x == box.xPos):
      continue
    elif(fullGrid[x][box.yPos].num == box.num):
      return False
  return True


#check to see if there are any other of the same letter in that column
def checkY(letter):
  i = 0
  while(i < a):
    if((inputs[i])[box.yPos] == box.letter):
      return True
    else:
      return False

#print grid
def printGrid(fullGrid, a):
  for y in range(a):
    print("")
    for x in range(a):
      print(fullGrid[x][y].num, end = ' ')
  print("")




def randomInit(fullGrid, a):
  for y in range(a):
    for x in range(a):
      fullGrid[x][y].num = random.randint(1,6)
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



a = int(input())
fullGrid = [[0 for x in range(6)] for y in range(6)]

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
printGrid(randomInit(fullGrid, a), a)
print(checkRow(fullGrid[0][0]))
