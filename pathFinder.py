#Idea: Path finder
#DIJKSTRA

mapOne = [
    ['#','#','#','#'],
    ['#',' ',' ',' '],
    ['#',' ','#',' '],
    ['#','O','#',' ']
]

MT = [
    ['#','#','#','#'],
    ['#',' ',' ','#'],
    ['#',' ','O','#'],
    ['#',' ','#','#']
]

MTH = [
    ['#','#','#','#','#'],
    ['#','O',' ',' ','#'],
    ['#','#','#',' ','#'],
    ['#',' ',' ',' ','#'],
    ['#',' ','#','#','#'],
]

mapTwo = [
    ['#','#','#','#','#','#'],
    ['#','#',' ',' ','O','#'],
    ['#','#',' ','#','#','#'],
    ['#','#',' ',' ',' ','#'],
    ['#','#','#','#',' ','#'],
    ['#','#','#','#','#','#']
]

hardMap = [
    ['#','#','#','#','#','#','#','#','#','#'],
    ['#','#','#','#','#','#','#','#',' ','#'],
    ['#','#',' ',' ',' ',' ',' ','#',' ','#'],
    ['#','#',' ','#','#','#',' ','#',' ','#'],
    ['O',' ',' ','#',' ','#',' ','#',' ','#'],
    ['#','#',' ','#',' ',' ',' ','#',' ','#'],
    ['#','#',' ','#','#','#','#','#',' ','#'],
    ['#','#',' ',' ',' ',' ',' ',' ',' ','#'],
    ['#','#','#','#','#','#','#','#','#','#'],
    ['#','#','#','#','#','#','#','#','#','#']
]

harderMap = [
    ['#','#','#','#','#','#','#','#','#','#'],
    ['#','#','#','#','#','#','#','#',' ','#'],
    ['#','#',' ',' ',' ',' ',' ','#',' ','#'],
    ['#','#',' ','#','#','#',' ','#',' ','#'],
    [' ',' ',' ','#',' ','#',' ','#',' ','#'],
    [' ','#',' ','#',' ',' ',' ','#',' ','#'],
    [' ','#',' ','#','#','#','#','#',' ','#'],
    [' ','#',' ',' ',' ',' ',' ',' ',' ','#'],
    [' ','#','#','#','#','#','#','#','#','#'],
    ['O','#','#','#','#','#','#','#','#','#']
]

#Recursive function to find a path to the labirinth
def FindPath(x, y, d, mapped, path=[], moves=0):
    #Up
    if(d == 0):
        if(mapped[y-1][x] == "O"):
            path.append([x,y-1])
            return path, moves
        elif(mapped[y][x-1] == " "):
            d = 1
            path.append([x-1,y])
            return FindPath(x-1, y, d, mapped, path, moves+1)
        elif(mapped[y-1][x] == "#"):
            d = 3
            return FindPath(x,y, d, mapped, path, moves+1)
        elif(mapped[y][x-1] == "#"):
            path.append([x,y-1])
            return FindPath(x,y-1, d, mapped, path, moves+1)
        else:
            d = 1
            path.append([x-1,y])
            return FindPath(x-1, y, d, mapped, path, moves+1)
    #Left
    elif(d == 1):
        if(mapped[y][x-1] == "O"):
            path.append([x-1,y])
            return path, moves
        elif(mapped[y+1][x] == " "):
            d = 2
            path.append([x,y+1])
            return FindPath(x, y+1, d, mapped, path, moves+1)
        elif(mapped[y][x-1] == "#"):
            d = 0
            return FindPath(x,y, d, mapped, path, moves+1)
        elif(mapped[y+1][x] == "#"):
            path.append([x-1,y])
            return FindPath(x-1,y, d, mapped, path, moves+1)
        else:
            d = 2
            path.append([x,y+1])
            return FindPath(x, y+1, d, mapped, path, moves+1)
    #Down
    elif(d == 2):
        if(mapped[y+1][x] == "O"):
            path.append([x,y+1])
            return path, moves
        elif(mapped[y][x+1] == " "):
            d = 3
            path.append([x+1,y])
            return FindPath(x+1, y, d, mapped, path, moves+1)
        elif(mapped[y+1][x] == "#"):
            d = 1
            return FindPath(x,y, d, mapped, path, moves+1)
        elif(mapped[y][x+1] == "#"):
            path.append([x,y+1])
            return FindPath(x,y+1, d, mapped, path, moves+1)
        else:
            d = 3
            path.append([x+1][y])
            return FindPath(x+1, y, d, mapped, path, moves+1)
    #Right
    elif(d == 3):
        if(mapped[y][x+1] == "O"):
            path.append([x,y+1])
            return path, moves
        elif(mapped[y-1][x] == " "):
            d = 0
            path.append([x,y-1])
            return FindPath(x, y-1, d, mapped, path, moves+1)
        elif(mapped[y][x+1] == "#"):
            d = 2
            return FindPath(x,y, d, mapped, path, moves+1)
        elif(mapped[y-1][x] == "#"):
            path.append([x+1,y])
            return FindPath(x+1,y, d, mapped, path, moves+1)
        else:
            d = 0
            path.append([x,y-1])
            return FindPath(x, y-1, d, mapped, path, moves+1)
    else:
        input("Something wrong Happend\n")
        exit(1)

print(FindPath(3,3,0,mapOne)[0])
print(FindPath(3,3,0,mapOne)[1])
print("")
print(FindPath(1,3,0,MT)[0])
print(FindPath(1,3,0,MT)[1])
print("")
print(FindPath(1,3,0,MTH)[0])
print(FindPath(1,3,0,MTH)[1])
print("")
print(FindPath(4,4,0,mapTwo)[0])
print(FindPath(4,4,0,mapTwo)[1])
print("")
print(FindPath(4,4,2,hardMap)[0])
print(FindPath(4,4,2,hardMap)[1])
print("")
print(FindPath(4,4,2,harderMap)[0])
print(FindPath(4,4,2,harderMap)[1])
