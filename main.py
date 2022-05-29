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
    bombs = mine
    rate = mine/(row*col)
    weight = [rate,100-rate]
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
    return [mines,bombs]

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
def isVaild(direction,current,flag):
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
    if flag :
        if (check[0]<0 or check[0] >= len(table)) or (check[1]<0 or check[1] >= len(table[0])) :
            return False
    elif (check in mines):
        return False
    return check
def addNumber(dic):
    for j in dic:
        for i in ["N","W","S","E","NE","NW","SE","SW"]:
            check = isVaild(i,j,0)
            if not check :
                dic[j] += 1
def goCheck(target,dic):
    mustcheck = []
    mustcheck.insert(0,target)
    show = []
    while mustcheck :
        current = mustcheck.pop()
        if dic[current] == 0:
            for i in ["N","W","S","E","NE","NW","SE","SW"] :
                check = isVaild(i,current,1)
                if check :
                    if check not in show:
                        show.append(check)
                        if dic[check] == 0:
                            mustcheck.insert(0,check)
        else:
            show.append(current)
                
    return show

def adjustTable(show,table,number):
    for i in show:
        if number[i] == 0 : table[i[0]][i[1]] = "⬜"
        if number[i] == 1 : table[i[0]][i[1]] = "1️⃣ "
        if number[i] == 2 : table[i[0]][i[1]] = "2️⃣ "
        if number[i] == 3 : table[i[0]][i[1]] = "3️⃣ "
        if number[i] == 4 : table[i[0]][i[1]] = "4️⃣ "
        if number[i] == 5 : table[i[0]][i[1]] = "5️⃣ "
        if number[i] == 6 : table[i[0]][i[1]] = "6️⃣ "
        if number[i] == 7 : table[i[0]][i[1]] = "7️⃣ "
        if number[i] == 8 : table[i[0]][i[1]] = "8️⃣ "
    return table
        
import random as rd
from time import sleep
mines,bombs = randomMines("medium")
table = createTable("medium")

print(mines)
for i in table:
    print("".join(i))
print()
death = 0
win = 0
number = {}
showed = []
for i in range(len(table)):
    for j in range(len(table[i])):
        number[(i,j)] = 0
for i in mines:
    number.pop(i)
addNumber(number)
allSafe = list(number.keys())
k=0
while not (death or win) :
    bombleft = 0
    while table[allSafe[k][0]][allSafe[k][1]] != "🟩":
        k+=1
    target = str(allSafe[k])
    # target = input()
    target = target.strip('(')
    target = target.strip(')')
    split = target.index(",")
    i = int(target[:split])
    j = int(target[split+1:])
    target = (i,j)
    if (i,j) in mines : 
        death = 1
        print("You're dead, try again later.")
    else:
      show = goCheck(target,number)
    showed = list(set(show+showed))
    table = adjustTable(show,table,number)
    for i in table:
        print("".join(i))
        bombleft += i.count("🟩")
        
    if bombleft == bombs:
        print("You defused all bomb! Congratulation.")
        win = 1
    k+=1
    print()
    sleep(0.2)