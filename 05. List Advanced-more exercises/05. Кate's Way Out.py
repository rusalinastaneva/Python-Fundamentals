rows=int(input())
maze=[list(input()) for i in range(rows)]
start=[(row,col) for row in range(rows) for col in range(len(maze[row])) if maze[row][col]=="k"][0]

exitPoint=[(row,col) for row in range(rows) for col in range(len(maze[row])) if maze[row][col]==" " and
           (row==rows-1 or row==0 or col==0 or col==len(maze[1])-1)][0]
washere=[]; correctPath=[]

for row in range(rows):
    washere.append([])
    correctPath.append([])
    for col in range(len(maze[row])):
        washere[row].append(False)
        correctPath[row].append(False)


def recursiveSolve(x, y):
    if x == exitPoint[0] and y== exitPoint[1]: return True  #If you reached the end
    elif maze[x][y] == "#" or washere[x][y]: return False   #If you are on a wall or already were here

    # mark as visited
    washere[x][y]=True

    if x != 0: # Checks if not on top edge
        if recursiveSolve(x - 1, y): # Recalls method one up
            correctPath[x][y] = True # Sets that path value to True;
            return True

    if x != rows  - 1: # Checks if not on bottom edge
        if recursiveSolve(x+1, y): # Recalls method one down
            correctPath[x][y] = True
            return True

    if y != 0: # Checks if not on left edge
        if recursiveSolve(x, y-1): # Recalls method one to the left
            correctPath[x][y] = True
            return True
    if y != len(maze[x]) - 1: # Checks if not on right edge
        if recursiveSolve(x, y+1): # Recalls method one to the right
            correctPath[x][y] = True
            return True
    return False

counter=1
res=recursiveSolve(start[0],start[1])
counter+=sum(sum(row) for row in correctPath)
if not res:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {counter} moves")