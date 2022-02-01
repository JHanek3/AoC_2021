# 3.1
# You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). 
# The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

# Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. 
# For example, given the following diagnostic report:

import numpy as np
from collections import Counter
report = [ "00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010" ]

def split(word):
    return [char for char in word]

def formatList(daList):
    listOLists = []
    for x in daList:
        listOLists.append(split(x))
    return np.array(listOLists).T.tolist()

def solution1a(daList):
    listT = formatList(daList)
    gamma = ""
    epsilon = ""
    for x in listT:
        res = Counter(x)
        res = max(res, key = res.get)
        gamma += str(res)
        
        res = Counter(x)
        res = min(res, key = res.get)
        epsilon += str(res)

    gamma = int(gamma,2)
    epsilon = int(epsilon,2)
    return gamma * epsilon

def solution1b():
    with open("3.txt") as f:
        report = []
        for line in f:
            cleanLine = line.strip()
            report.append(cleanLine)
    print(solution1a(report))

print(solution1a(report))
solution1b()
print("-" * 20)

# 3.2
# I'm not even going to try and explain this one

def solution2a(daList):
    for x in range(len(daList[0])):
        if x == 0:
            prevList = daList
        else:
            prevList = newList
        
        if len(prevList) == 1:
            break

        listT = formatList(prevList)
        newList = []
        
        frequency = Counter(listT[x])
            
        if frequency["1"] > frequency["0"] or frequency["1"] == frequency["0"]:
            comparator = "1"
        else:
            comparator = "0"

        for y in prevList:
            if y[x] == comparator:
                newList.append(y)
    oxygen = int("".join(newList),2)
    
    for x in range(len(daList[0])):
        if x == 0:
            prevList = daList
        else:
            prevList = newList
        
        if len(prevList) == 1:
            break

        listT = formatList(prevList)
        newList = []

        frequency = Counter(listT[x])
            
        if frequency["0"] < frequency["1"] or frequency["1"] == frequency["0"]:
            comparator = "0"
        else:
            comparator = "1"

        for y in prevList:
            if y[x] == comparator:
                newList.append(y)
    carbon = int("".join(newList),2)
    return oxygen * carbon

print(solution2a(report))

def solution2b():
    with open("3.txt") as f:
        report = []
        for line in f:
            cleanLine = line.strip()
            report.append(cleanLine)
    print(solution2a(report))

solution2b()