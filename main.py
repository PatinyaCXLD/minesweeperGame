def randomMines(mode):
    mode.lower()
    if mode == "hard" :
        mine = 99
        row = 24
        col = 20
    elif mode == "medium" :
        mine = 40
        row = 18
        col = 14
    elif mode == "easy":
        mine = 10
        row = 10
        col = 8
    mines = []
    weight = [mine/(row*col),100-(mine/(row*col))]
    while mine > 0: 
        for i in range(col):
            if mine == 0 : break
            for j in range(row):
                if mine > 0 and (i,j) not in mines:
                    cell = rd.choices([1,0],weights= weight)
                    if cell == [1] :
                        mine-=1
                        mines.append((i,j))
                else : break
    return mines

def createTable(mode):
    if mode == "hard" :
        row = 24
        col = 20
    elif mode == "medium" :
        row = 18
        col = 14
    elif mode == "easy":
        row = 10
        col = 8
    table = []
    line = []
    for i in range(col):
        for j in range(row):
            line.append("🟩")
        table.append(line[:])
        line.clear()
    
    return table
def isVaild(direction,current):
    if direction == "N":
        check = (current[0]-1,current[1])
    if direction == "W":
        check = (current[0],current[1]-1)
    if direction == "S":
        check = (current[0]+1,current[1])
    if direction == "E":
        check = (current[0],current[1]+1)
    if direction == "NE":
        check = (current[0]-1,current[1]+1)
    if direction == "NW":
        check = (current[0]-1,current[1]-1)
    if direction == "SE":
        check = (current[0]+1,current[1]+1)
    if direction == "SW":
        check = (current[0]+1,current[1]-1)
    if (check[0]<0 or check[0] >= len(table)) or (check[1]<0 or check[1] >= len(table[0])) :
        return False
    elif (check in mines):
        return False
    return check
def addNumber(dic,mines):
    for j in mines:
        for i in ["N","W","S","E","NE","NW","SE","SW"]:
            check = isVaild(i,j)
            if check :
                dic[(check[0],check[1])] += 1

import random as rd

mines = randomMines("easy")
table = createTable("easy")

print(mines)
for i in table:
    print("".join(i))
    
death = 0
win = 0
number = {}
for i in range(len(table)):
    for j in range(len(table[i])):
        number[(i,j)] = 0
while not (death or win) :
    target = input()
    target.strip("(")
    target.strip(")")
    split = target.index(",")
    i = int(target[0:split])
    j = int(target[split+1:])
    addNumber(number,mines)
    death = 1
print(i,j)
print(number)
