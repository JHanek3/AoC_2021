# Day 6
# Each lantern fish creates a new lantern fish every 7 days
# A lantern fish creates a new fish resets its timer to 6, not 7 because 0 is a valid time value
# A new lantern fish starts with a internal timer of 8 and does not start counting down until the next day
# Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while each other number decreases by 1 if it was present at the start of the day

input = [3, 4, 3, 1, 2]
from collections import deque, Counter

def createFishDics(daList):
    fishDics = {}
    for x in range(len(daList)):
        fishDics[x] = daList[x]
    return fishDics

def theDaysHandler(fishDics, numDays):
    # length of days
    for x in range(numDays):
        # fishDics is a giant list of fish with their attributes
         # go through all the fish
        for fish, timer in list(fishDics.items()):

            # if the timer is 0, reset the timer back to six
            # then add a new fish at the end of the dictionary with the reproductive value of 8
            if timer == 0:
                fishDics[fish] = 6
                fishDics[len(fishDics)] = 8
            # otherwise just subtract 1 from the reproduction timer
            else:
                fishDics[fish] = timer - 1
    # print(f"{numDays} \n{fishDics} \n--------------------------------------")
    # After you've gone through the length of days, count how many fish exist in the list
    print(len(fishDics))
    
def solution1a():
    fishDics = createFishDics(input)
    theDaysHandler(fishDics, 80)

#solution1a()

def solution1b():
    input = [3,4,1,1,5,1,3,1,1,3,5,1,1,5,3,2,4,2,2,2,1,1,1,1,5,1,1,1,1,1,3,1,1,5,4,1,1,1,4,1,1,1,1,2,3,2,5,1,5,1,2,1,1,1,4,1,
    1,1,1,3,1,1,3,1,1,1,1,1,1,2,3,4,2,1,3,1,1,2,1,1,2,1,5,2,1,1,1,1,1,1,4,1,1,1,1,5,1,4,1,1,1,3,3,1,3,1,3,1,4,1,1,1,1,1,4,5,1,
    1,3,2,2,5,5,4,3,1,2,1,1,1,4,1,3,4,1,1,1,1,2,1,1,3,2,1,1,1,1,1,4,1,1,1,4,4,5,2,1,1,1,1,1,2,4,2,1,1,1,2,1,1,2,1,5,1,5,2,5,5,
    1,1,3,1,4,1,1,1,1,1,1,1,4,1,1,4,1,1,1,1,1,2,1,2,1,1,1,5,1,1,3,5,1,1,5,5,3,5,3,4,1,1,1,3,1,1,3,1,1,1,1,1,1,5,1,3,1,5,1,1,4,
    1,3,1,1,1,2,1,1,1,2,1,5,1,1,1,1,4,1,3,2,3,4,1,3,5,3,4,1,4,4,4,1,3,2,4,1,4,1,1,2,1,3,1,5,5,1,5,1,1,1,5,2,1,2,3,1,4,3,3,4,3]
    fishDics = createFishDics(input)
    theDaysHandler(fishDics, 80)
# solution2a()
# everything works up to here, then theres memory issues

def daysHandler1(list, numDays):
    counter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    counter = sorted(Counter(list).items())

    counter = [x[-1] for x in counter]
    counter.insert(0, 0)
    counter = counter + [0, 0, 0, 0]

    for i in range(numDays):
        # rotate the list
        counter = deque(counter)
        counter.rotate(-1)
        
        # convert deque back to list then edit values for reproduction
        counter = [x for x in counter]
        prevValue = counter[6]
        counter[6] = prevValue + counter[-1]
    print(sum(counter))

def solution1b():
    input = [3,4,1,1,5,1,3,1,1,3,5,1,1,5,3,2,4,2,2,2,1,1,1,1,5,1,1,1,1,1,3,1,1,5,4,1,1,1,4,1,1,1,1,2,3,2,5,1,5,1,2,1,1,1,4,1,
    1,1,1,3,1,1,3,1,1,1,1,1,1,2,3,4,2,1,3,1,1,2,1,1,2,1,5,2,1,1,1,1,1,1,4,1,1,1,1,5,1,4,1,1,1,3,3,1,3,1,3,1,4,1,1,1,1,1,4,5,1,
    1,3,2,2,5,5,4,3,1,2,1,1,1,4,1,3,4,1,1,1,1,2,1,1,3,2,1,1,1,1,1,4,1,1,1,4,4,5,2,1,1,1,1,1,2,4,2,1,1,1,2,1,1,2,1,5,1,5,2,5,5,
    1,1,3,1,4,1,1,1,1,1,1,1,4,1,1,4,1,1,1,1,1,2,1,2,1,1,1,5,1,1,3,5,1,1,5,5,3,5,3,4,1,1,1,3,1,1,3,1,1,1,1,1,1,5,1,3,1,5,1,1,4,
    1,3,1,1,1,2,1,1,1,2,1,5,1,1,1,1,4,1,3,2,3,4,1,3,5,3,4,1,4,4,4,1,3,2,4,1,4,1,1,2,1,3,1,5,5,1,5,1,1,1,5,2,1,2,3,1,4,3,3,4,3]
    daysHandler1(input, 80)

# solution1b()

def solution2a():
    # this breaks down to due to memory, lets try something else
    # fishDics = createFishDics(input)
    # theDaysHandler(fishDics, 256)
    daysHandler1(input, 256)
# solution2a()

def solution2b():
    report = [3,4,1,1,5,1,3,1,1,3,5,1,1,5,3,2,4,2,2,2,1,1,1,1,5,1,1,1,1,1,3,1,1,5,4,1,1,1,4,1,1,1,1,2,3,2,5,1,5,1,2,1,1,1,4,1,
    1,1,1,3,1,1,3,1,1,1,1,1,1,2,3,4,2,1,3,1,1,2,1,1,2,1,5,2,1,1,1,1,1,1,4,1,1,1,1,5,1,4,1,1,1,3,3,1,3,1,3,1,4,1,1,1,1,1,4,5,1,
    1,3,2,2,5,5,4,3,1,2,1,1,1,4,1,3,4,1,1,1,1,2,1,1,3,2,1,1,1,1,1,4,1,1,1,4,4,5,2,1,1,1,1,1,2,4,2,1,1,1,2,1,1,2,1,5,1,5,2,5,5,
    1,1,3,1,4,1,1,1,1,1,1,1,4,1,1,4,1,1,1,1,1,2,1,2,1,1,1,5,1,1,3,5,1,1,5,5,3,5,3,4,1,1,1,3,1,1,3,1,1,1,1,1,1,5,1,3,1,5,1,1,4,
    1,3,1,1,1,2,1,1,1,2,1,5,1,1,1,1,4,1,3,2,3,4,1,3,5,3,4,1,4,4,4,1,3,2,4,1,4,1,1,2,1,3,1,5,5,1,5,1,1,1,5,2,1,2,3,1,4,3,3,4,3]
    daysHandler1(report,256)
    # fishDics = createFishDics(input)
    # theDaysHandler(fishDics, 128)

solution2b()


