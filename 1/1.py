# 1.1
# To do this, count the number of times a depth measurement increases from the previous measurement.
# example input should return 7

# 1.2
# Start by comparing the first and second three-measurement windows. 
# The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. 
# The second window is marked B (200, 208, 210); its sum is 618. 
# The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.
# # example input should return 5
report = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

# from os import path
# with open("1.txt") as f:
#     report = []
#     for line in f:
#         cleanLine = int(line.strip())
#         report.append(cleanLine)

def solution1():
    increment = 0
    for x in range(len(report)):
        if x != 0:
            if report[x - 1] < report[x]:
                increment += 1
    print(increment)

def solution2():
    increment = 0
    for x in range(len(report)):
        try :
            if x != 0:
                previous = report[x - 1] + report[x] + report[x + 1]
                next = report [x] + report[x + 1] + report[x + 2]
                if previous < next:
                    increment += 1
        except:
            break
    print(increment)

solution1()
solution2()