import numpy
import random


#check to see if there are any other of the same letter in that row
def checkX(box):
  i = 0
  while(i < a):
    if((inputs[box.yPos])[i] == box.letter):
      return True
    else:
      return False


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
      print(fullGrid[y][x].num, end = ' ')
  print("")



def randomInit(fullGrid, a):
  for y in range(a):
    for x in range(a):
      fullGrid[y][x].num = random.randint(1,6)
  return fullGrid




class Section:
  def __init__(self, letter, numEls):
    self.letter = letter
    self.numEls = numEls

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

  def printBox(self):
    print("Box letter is " + self.letter + " at " + str(self.xPos)
          + ", " + str(self.yPos))



a = int(input())
inputs = []
boxes = []
fullGrid = [[0 for x in range(6)] for y in range(6)]
lastSection = Section("Z", 0)
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
    fullGrid[y][x] = newBox
    x += 1

  y += 1

while(
    
print(a)
print(inputs)
printGrid(randomInit(fullGrid, a), a)


