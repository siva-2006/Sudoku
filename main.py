from random import choice, randint
from time import sleep

def createGrid():
  grid = [[0 for i in range(9)] for i in range(9)]
  for k in range(3):
    nums = [i for i in range(1, 10)]
    for i in range(3):
      for j in range(3):
        num = choice(nums)
        nums.remove(num)
        grid[i + 3 * k][j + 3 * k] = num
  return grid


def solveGrid(grid):
  find = find_empty(grid)
  if not find:
    return True
  else:
    row, col = find

  for i in range(1, 10):
    if isValid(grid, i, (row, col)):
      grid[row][col] = i

      if solveGrid(grid):
        return True

      grid[row][col] = 0

  return False


def isValid(grid, num, pos):
  # Check Row
  for i in range(9):
    if grid[pos[0]][i] == num and pos[1] != i:
      return False

  # Check Column
  for i in range(9):
    if grid[i][pos[1]] == num and pos[0] != i:
      return False

  # Check Box
  box_x = pos[1] // 3
  box_y = pos[0] // 3

  for i in range(box_y * 3, box_y * 3 + 3):
    for j in range(box_x * 3, box_x * 3 + 3):
      if grid[i][j] == num and (i, j) != pos:
        return False

  return True


def find_empty(grid):
  for i in range(9):
    for j in range(9):
      if grid[i][j] == 0:
        return (i, j)  #row, column
  return None


def unsolveGrid(grid, choice):
  value = {"1": randint(40,45), "2": randint(45, 50), "3": randint(50, 55)}
  unslved = []
  indexes = []
  i = 0
  while i <= value[choice]:
    x = randint(0, 8)
    y = randint(0, 8)
    if (x, y) not in indexes:
      indexes += [(x, y)]
      i += 1
  for i in range(len(grid)):
    temp = []
    for j in range(len(grid[0])):
      if (i, j) in indexes:
        temp += [0]
      else:
        temp += [grid[i][j]]
    unslved += [temp]
  return unslved


def isCorrect(solvedGrid, rcn):
  if solvedGrid[rcn[0] - 1][rcn[1] - 1] == rcn[2]: return True
  else: return False


def printGrid(grid):
  for i in range(9):
    if i % 3 == 0 and i != 0:
      for k in range(21):
        print("▬", end="")
      print()
    for j in range(9):
      if j % 3 == 0 and j != 0:
        print("┃", end=" ")
      if grid[i][j] == 0:
        print(" ", end=" ")
      else:
        print(grid[i][j], end=" ")
      if j == 8:
        print()


print("""
░██████╗██╗░░░██╗██████╗░░█████╗░██╗░░██╗██╗░░░██╗
██╔════╝██║░░░██║██╔══██╗██╔══██╗██║░██╔╝██║░░░██║
╚█████╗░██║░░░██║██║░░██║██║░░██║█████═╝░██║░░░██║
░╚═══██╗██║░░░██║██║░░██║██║░░██║██╔═██╗░██║░░░██║
██████╔╝╚██████╔╝██████╔╝╚█████╔╝██║░╚██╗╚██████╔╝
╚═════╝░░╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝░╚═════╝░
""")
while True:
  print("""
▄█░ 　 ░ 　 ▒█▀▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ 
░█░ 　 ▄ 　 ░▀▀▀▄▄ ░░█░░ █▄▄█ █▄▄▀ ░░█░░ 
▄█▄ 　 █ 　 ▒█▄▄▄█ ░░▀░░ ▀░░▀ ▀░▀▀ ░░▀░░ 

█▀█ 　 ░ 　 ▒█▀▀█ █░░█ █░░ █▀▀ █▀▀ 
░▄▀ 　 ▄ 　 ▒█▄▄▀ █░░█ █░░ █▀▀ ▀▀█ 
█▄▄ 　 █ 　 ▒█░▒█ ░▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ 

█▀▀█ 　 ░ 　 ▒█▀▀█ █░░█ ░▀░ ▀▀█▀▀ 
░░▀▄ 　 ▄ 　 ▒█░▒█ █░░█ ▀█▀ ░░█░░ 
█▄▄█ 　 █ 　 ░▀▀█▄ ░▀▀▀ ▀▀▀ ░░▀░░
""")
  ch = input()
  if ch == "1":

    print("""
▄█░ 　 ░ 　 ▒█▀▀▀ █▀▀█ █▀▀ █░░█ 
░█░ 　 ▄ 　 ▒█▀▀▀ █▄▄█ ▀▀█ █▄▄█ 
▄█▄ 　 █ 　 ▒█▄▄▄ ▀░░▀ ▀▀▀ ▄▄▄█ 

█▀█ 　 ░ 　 ▒█▀▄▀█ █▀▀ █▀▀▄ ░▀░ █░░█ █▀▄▀█ 
░▄▀ 　 ▄ 　 ▒█▒█▒█ █▀▀ █░░█ ▀█▀ █░░█ █░▀░█ 
█▄▄ 　 █ 　 ▒█░░▒█ ▀▀▀ ▀▀▀░ ▀▀▀ ░▀▀▀ ▀░░░▀ 

█▀▀█ 　 ░ 　 ▒█░▒█ █▀▀█ █▀▀█ █▀▀▄ 
░░▀▄ 　 ▄ 　 ▒█▀▀█ █▄▄█ █▄▄▀ █░░█ 
█▄▄█ 　 █ 　 ▒█░▒█ ▀░░▀ ▀░▀▀ ▀▀▀░ 

░█▀█░ 　 ░ 　 ▒█▀▀█ █▀▀█ █▀▀ █░█ 
█▄▄█▄ 　 ▄ 　 ▒█▀▀▄ █▄▄█ █░░ █▀▄ 
░░░█░ 　 █ 　 ▒█▄▄█ ▀░░▀ ▀▀▀ ▀░▀
""")
    ch1 = input()
    if ch1 in "123":
      diff = ch1
      grid = createGrid()
      solveGrid(grid)
      solvedGrid = []
      for q in grid:
        solvedGrid += [q]
      unsolvedGrid = unsolveGrid(grid, diff)
      print("""
▒█▀▀█ █▀▀ █▀▀▄ █▀▀ █▀▀█ █▀▀█ ▀▀█▀▀ ░▀░ █▀▀▄ █▀▀▀ 
▒█░▄▄ █▀▀ █░░█ █▀▀ █▄▄▀ █▄▄█ ░░█░░ ▀█▀ █░░█ █░▀█ 
▒█▄▄█ ▀▀▀ ▀░░▀ ▀▀▀ ▀░▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀░░▀ ▀▀▀▀ 

▒█▀▀█ █░░█ ▀▀█ ▀▀█ █░░ █▀▀ ░ ░ ░ 
▒█▄▄█ █░░█ ▄▀░ ▄▀░ █░░ █▀▀ ▄ ▄ ▄ 
▒█░░░ ░▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ █ █ █
""")
      sleep(1.5)
      printGrid(unsolvedGrid)
      strike = 0
      while strike < 3:
        rcn = list(
          eval(
            input(
              "\nEnter Row, Column, Number(Enter \"Q\" with quotes to give up):"
            )))
        print()
        if rcn == ["Q"]:
          print("Are you sure?(y/n)")
          ch2 = input()
          print()
          if ch2.lower() == "y":
            printGrid(solvedGrid)
            print()
            break
        elif len(rcn) != 3:
          print("Invalid input...")
        elif type(rcn[0]) is not int or type(rcn[1]) is not int or type(
            rcn[2]) is not int:
          print("Invalid input...")
        elif rcn[2] > 9 or rcn[2] < 1:
          print("Number must be between 1-9...")
        elif rcn[1] > 9 or rcn[1] < 1:
          print("Column must be between 1-9...")
        elif rcn[0] > 9 or rcn[0] < 1:
          print("Row must be between 1-9...")
        elif unsolvedGrid[rcn[0] - 1][rcn[1] - 1] != 0:
          print("Cannot fill already filled space...")
        else:
          if isCorrect(solvedGrid, rcn):
            unsolvedGrid[rcn[0] - 1][rcn[1] - 1] = rcn[2]
            printGrid(unsolvedGrid)
            if grid == unsolvedGrid:
              print("""
█▀█ █░█ ▀█ ▀█ █░░ █▀▀   █▀▀ █▀█ █▀▄▀█ █▀█ █░░ █▀▀ ▀█▀ █▀▀ █▀▄ █
█▀▀ █▄█ █▄ █▄ █▄▄ ██▄   █▄▄ █▄█ █░▀░█ █▀▀ █▄▄ ██▄ ░█░ ██▄ █▄▀ ▄
""")
              break
          else:
            strike += 1
            print(f"Strike {strike}!")
      else:
        print("""
░██████╗░░█████╗░███╗░░░███╗███████╗
██╔════╝░██╔══██╗████╗░████║██╔════╝
██║░░██╗░███████║██╔████╔██║█████╗░░
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝

░█████╗░██╗░░░██╗███████╗██████╗░██╗
██╔══██╗██║░░░██║██╔════╝██╔══██╗██║
██║░░██║╚██╗░██╔╝█████╗░░██████╔╝██║
██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗╚═╝
╚█████╔╝░░╚██╔╝░░███████╗██║░░██║██╗
░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝
""")
        printGrid(solvedGrid)

  elif ch == "2":
    print("""\n - Each row must contain the numbers 1-9 exactly once.
 - Each column must contain the numbers 1-9 exactly once.
 - Each 3×3 box must contain the numbers 1-9 exactly once.
 - 3 Wrong guesses will lead to a game over""")
  elif ch == "3":
    print("""
████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗
╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║
░░░██║░░░███████║███████║██╔██╗██║█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║
░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║
░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░

                     ███████╗░█████╗░██████╗░
                     ██╔════╝██╔══██╗██╔══██╗
                     █████╗░░██║░░██║██████╔╝
                     ██╔══╝░░██║░░██║██╔══██╗
                     ██║░░░░░╚█████╔╝██║░░██║
                     ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝

      ██████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗███╗░░██╗░██████╗░██╗
      ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██║████╗░██║██╔════╝░██║
      ██████╔╝██║░░░░░███████║░╚████╔╝░██║██╔██╗██║██║░░██╗░██║
      ██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██║██║╚████║██║░░╚██╗╚═╝
      ██║░░░░░███████╗██║░░██║░░░██║░░░██║██║░╚███║╚██████╔╝██╗
      ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝""")
    break
  else:
    print("Invalid Choice...")
