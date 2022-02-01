input = [
    "0199043210",
    "3987894921",
    "9856789892",
    "0067896789",
    "9899965678",
]

def lowPoints(daList):
    lowPoints = []
    for index1, element in enumerate(daList):
        lengthElement = len(str(element))
        if element == daList[0]:
            for index2, number in enumerate(str(element)):
                
                if index2 == 0:
                    subscriptRight = str(element)[index2+ 1]
                    subscriptDown = daList[index1 + 1]
                    subscriptDown = str(subscriptDown)[index2]

                    if int(number) < int(subscriptRight) and int(number) < int(subscriptDown):
                        lowPoints.append(int(number))
                
                elif index2 == lengthElement - 1:
                    subscriptString = str(element)
                    subscriptLeft = subscriptString[index2 - 1]

                    subscriptString= daList[index1 + 1]
                    subscriptString = str(subscriptString)
                    subscriptDown = subscriptString[index2]

                    if int(number) < int(subscriptLeft) and int(number) < int(subscriptDown):
                        lowPoints.append(int(number))
                    
                
                else:
                    subscriptString = str(element)
                    subscriptLeft = subscriptString[index2 - 1]
                    subscriptRight = subscriptString[index2 + 1]

                    subscriptString= daList[index1 + 1]
                    subscriptString = str(subscriptString)
                    subscriptDown = subscriptString[index2]
                    
                    if int(number) < int(subscriptLeft) and int(number) < int(subscriptRight) and int(number) < int(subscriptDown):
                        lowPoints.append(int(number))

        elif element == daList[-1]:
            for index2, number in enumerate(str(element)):
                if index2 == 0:
                    subscriptRight = str(element)[index2+ 1]
                    subscriptUp = daList[index1 - 1]
                    subscriptUp = str(subscriptUp)[index2]

                    if int(number) < int(subscriptRight) and int(number) < int(subscriptUp):
                        lowPoints.append(int(number))
                
                elif index2 == lengthElement - 1:
                    subscriptString = str(element)
                    subscriptLeft = subscriptString[index2 - 1]

                    subscriptString= daList[index1 - 1]
                    subscriptString = str(subscriptString)
                    subscriptUp = subscriptString[index2]

                    if int(number) < int(subscriptLeft) and int(number) < int(subscriptUp):
                        lowPoints.append(int(number))     
                else:
                    subscriptString = str(element)
                    subscriptLeft = subscriptString[index2 - 1]
                    subscriptRight = subscriptString[index2 + 1]

                    subscriptString= daList[index1 - 1]
                    subscriptString = str(subscriptString)
                    subscriptUp = subscriptString[index2]
                    
                    if int(number) < int(subscriptLeft) and int(number) < int(subscriptRight) and int(number) < int(subscriptUp):
                        lowPoints.append(int(number))
        
        else:
            for index2, number in enumerate(str(element)):
                if index2 == 0:
                    subscriptRight = str(element)[index2+ 1]
                    subscriptUp = daList[index1 - 1]
                    subscriptUp = str(subscriptUp)[index2]
                    subscriptDown = daList[index1 + 1]
                    subscriptDown = str(subscriptUp)[index2]

                    if int(number) < int(subscriptRight) and int(number) < int(subscriptUp) and int(number) < int(subscriptDown):
                        lowPoints.append(int(number))
                
                elif index2 == lengthElement - 1:
                    subscriptString = str(element)
                    subscriptLeft = subscriptString[index2 - 1]

                    subscriptString= daList[index1 - 1]
                    subscriptString = str(subscriptString)
                    subscriptUp = subscriptString[index2]

                    subscriptDown = daList[index1 + 1]
                    subscriptDown = str(subscriptDown)[index2]

                    if int(number) < int(subscriptLeft) and int(number) < int(subscriptUp) and int(number) < int(subscriptDown):
                        lowPoints.append(int(number))
                else:
                        subscriptString = str(element)
                        subscriptLeft = subscriptString[index2 - 1]
                        subscriptRight = subscriptString[index2 + 1]

                        subscriptString= daList[index1 - 1]
                        subscriptString = str(subscriptString)
                        subscriptUp = subscriptString[index2]
                        
                        subscriptDown = daList[index1 + 1]
                        subscriptDown = str(subscriptDown)[index2]
                    
                        if int(number) < int(subscriptLeft) and int(number) < int(subscriptRight) and int(number) < int(subscriptUp) and int(number) < int(subscriptDown):
                            lowPoints.append(int(number))

    print(sum(lowPoints))
    print(lowPoints)

def solution1a():
    lowPoints(input)

solution1a()

def solution2a():
    report = []
    with open("9.txt") as f:
        for line in f:
            report.append(line.strip())
    # print(input)
    lowPoints(report)

solution2a()