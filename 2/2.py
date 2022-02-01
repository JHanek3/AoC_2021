# 2.1
# After following these instructions, 
# you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)
# Calculate the horizontal position and depth you would have after following the planned course. 
# What do you get if you multiply your final horizontal position by your final depth?

from os import path
report = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

def solution1a(daList):
    sums = { "horizontal": 0, "depth": 0}
    for x in range(len(daList)):
        split = daList[x].split(" ")
        if split[0] == "forward":
            sums["horizontal"] += int(split[1])
        elif split[0] == "down":
            sums["depth"] += int(split[1])
        else:
            sums["depth"] -= int(split[1])
    print(sums["horizontal"] * sums["depth"])

solution1a(report)

def solution1b():
    with open("2.txt") as f:
        report = []
        for line in f:
            cleanLine = line.strip()
            report.append(cleanLine)
    solution1a(report)

solution1b()
print("-" * 20)

# 2.2
# down x increases your aim by x units
# up x decreases your aim by x units
# forward x does two things
# increases your horizontal position by x units
# increases your depth by your aim bultiplied by x

def solution2a(daList):
    sums = { "horizontal": 0, "depth": 0, "aim": 0}
    for x in daList:
        split = x.split(" ")
        if split[0] == "forward":
            sums["horizontal"] += int(split[1])
            sums["depth"] += sums["aim"] * int(split[1])
        elif split[0] == "down":
            sums["aim"] += int(split[1])
        else:
            sums["aim"] -= int(split[1])
    print(sums["horizontal"] * sums["depth"])

solution2a(report)

def solution2b():
    with open("2.txt") as f:
        report = []
        for line in f:
            cleanLine = line.strip()
            report.append(cleanLine)
    solution2a(report)

solution2b()