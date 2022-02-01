# Day 5 Hydrothermal Vents

input = [ "0,9 -> 5,9", "8,0 -> 0,8", "9,4 -> 3,4", "2,2 -> 2,1", "7,0 -> 7,4", "6,4 -> 2,0", "0,9 -> 2,9", "3,4 -> 1,4", "0,0 -> 8,8", "5,5 -> 8,2"]

def getGridSize(daList):
    xMin = 0
    xMax = 0
    yMin = 0
    yMax = 0
    for x in daList:
        x = x.split("->")
        for coordinate in x:
            coordinate = coordinate.replace(" ", "")
            coordinate = coordinate.split(",")

            if int(coordinate[0]) < xMin:
                xMin = int(coordinate[0])
            if int(coordinate[0]) > xMax:
                xMax = int(coordinate[0])
            if int(coordinate[1]) < yMin:
                yMin = int(coordinate[1])
            if int(coordinate[1]) > yMax:
                yMax = int(coordinate[1])
            
    return [(xMin, yMin), (xMax, yMax)]

def createGrid(daCoordinates):
    grid = []
    # print(daCoordinates)
    for y in range(daCoordinates[1][1] + 1):
        row = []
        for x in range(daCoordinates[1][0] + 1):
            row.append(".")
        grid.append(row)
    return grid

def updateGrid(daCoordinates, grid):
    daCoordinates = daCoordinates.split("->")
    daCoordinates = [coordinates.strip() for coordinates in daCoordinates]
    # print(daCoordinates)
    x1 = int(daCoordinates[0].split(",")[0])
    y1 = int(daCoordinates[0].split(",")[1])
    x2 = int(daCoordinates[1].split(",")[0])
    y2 = int(daCoordinates[1].split(",")[1])
    
    # Focuses on Horizontal and Vertical
    if x1 == x2:
        if y1 > y2:
            for y in range(y2, y1 + 1):
                if grid[y][x1] == ".":
                    grid[y][x1] = "1"
                else:
                    grid[y][x1] = str(int(grid[y][x1]) + 1)
        
        if y1 < y2:
            for y in range(y1, y2 + 1):
                if grid[y][x1] == ".":
                    grid[y][x1] = "1"
                else:
                    grid[y][x1] = str(int(grid[y][x1]) + 1)
    
    
    if y1 == y2:
        if x1 > x2:
            for x in range(x2, x1 + 1):
                if grid[y1][x] == ".":
                    grid[y1][x] = "1"
                else:
                    grid[y1][x] = str(int(grid[y1][x]) + 1)
        
        if x1 < x2:
            for x in range(x1, x2 + 1):
                if grid[y1][x] == ".":
                    grid[y1][x] = "1"
                else:
                    grid[y1][x] = str(int(grid[y1][x]) + 1)

    # Now to add diagonal
    if x1 > x2 and y2 < y1:
        difference = x1 - x2
        for x in range(difference + 1):
            if grid[y2 + x][x2 + x] == ".":
                grid[y2 + x][x2 + x] = "1"
            else:
                grid[y2 + x][x2 + x] = str(int(grid[y2 + x][x2 + x]) + 1)
            
    if x1 > x2 and y2 > y1:
        difference = x1 - x2
        for x in range(difference + 1):
            if grid[y2 - x][x2 + x] == ".":
                grid[y2 - x][x2 + x] = "1"
            else:
                grid[y2 - x][x2 + x] = str(int(grid[y2 - x][x2 + x]) + 1)

    if x1 < x2 and y1 < y2:
        difference = y2 - y1
        for x in range(difference + 1):
            if grid[y1 + x][x1 + x] == ".":
                grid[y1 + x][x1 + x] = "1"
            else:
                grid[y1 + x][x1 + x] = str(int(grid[y1 + x][x1 + x]) + 1)
            
    if x1 < x2 and y1 > y2:
        difference = y1 - y2
        for x in range(difference + 1):
            if grid[y1 - x][x1 + x] == ".":
                grid[y1 - x][x1 + x] = "1"
            else:
                grid[y1 - x][x1 + x] = str(int(grid[y1 - x][x1 + x]) + 1)

def determineOverlap(grid):
    overlap = 0
    for y in grid:
        for x in y:
            try:
                if int(x) >= 2:
                    overlap += 1
            except ValueError:
                pass
    print(overlap)

def solution1a():
    grid = createGrid(getGridSize(input))
    # updateGrid("2,2 -> 2,1", grid)
    # updateGrid("2,2 -> 2,4", grid)
    # updateGrid("6,6 -> 6,5", grid)
    # updateGrid("7,7 -> 5,7", grid)
    for x in input:
        updateGrid(x, grid)
    for x in grid:
        print(x)
    determineOverlap(grid)

# solution1a()

def solution1b():
    with open("5.txt") as f:
        report = []
        for line in f:
            cleanLine = line.strip()
            report.append(cleanLine)
    grid = createGrid(getGridSize(report))
    for x in report:
        updateGrid(x, grid)
    determineOverlap(grid)
# solution1b()

def solution2a():
    grid = createGrid(getGridSize(input))
    for x in input:
        updateGrid(x, grid)

    for x in grid:
        print(x)
    
    determineOverlap(grid)

# solution2a()

def solution2b():
    with open("5.txt") as f:
        report = []
        for line in f:
            cleanLine = line.strip()
            report.append(cleanLine)
    grid = createGrid(getGridSize(report))
    for x in report:
        updateGrid(x, grid)
    determineOverlap(grid)

solution2b()