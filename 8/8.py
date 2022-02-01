from collections import Counter
import re

# Lol, I'm not writing this description
daStr = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"
daList = [  "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
            "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
            "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
            "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
            "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
            "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
            "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
            "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
            "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
            "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"]
def counterStr(str):
    strCount = 0

    newStr = str.split("|")
    newStr = "".join(newStr[1]).strip()
    
    numbers = newStr.split(" ")
    for number in numbers:
        counter = sum(Counter(number).values())
        if counter == 2 or counter == 3 or counter == 4 or counter == 7:
            strCount +=1
    
    return strCount



def solution1a():
    overallCount = 0
    for str in daList:
        overallCount += counterStr(str)
    print(overallCount)

# solution1a()

def solution2a():
    overallCount = 0
    with open("8.txt") as f:
        report = []
        for line in f:
            cleanLine = line.strip()
            report.append(cleanLine)
    for str in report:
        overallCount += counterStr(str)
    print(overallCount)
# solution2a()

def containsAll(strTest, strBase):
    daSet = set(strBase)
    return 0 not in [c in strTest for c in daSet]

def markersCreator(daStr):
    markers = {"Top": "", "LT": "", "RT": "", "Center": "", "LB": "", "RB": "", "Bottom": ""}
    numbers = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
    newStr = daStr.split("|")
    decoder = "".join(newStr[0]).strip()
    # numbers = "".join(newStr[1]).strip()
    
    # initial setUp
    decoderList = decoder.split(" ")

    for item in decoderList:
        if len(item) == 2:
            numbers[1] = item
        elif len(item) == 3:
            numbers[7] = item
        elif len(item) == 4:
            numbers[4] = item
        elif len(item) == 7:
            numbers[8] = item
    
    # Get Top
    one = set(numbers[1])
    seven = set(numbers[7])
    markers["Top"] = "".join(seven - one)

    eight = set(numbers[8])
    decorderList1 = []
    # Get RT & RB
    for decoder in decoderList:
        if len(decoder) == 6:
            if not containsAll(decoder, numbers[7]):
                numbers[6] = decoder
                six = set(decoder)
                markers["RT"] = "".join(seven - six)
                markers["RB"] = "".join(one- (seven - six))
            else:
                decorderList1.append(decoder)
        else:
            decorderList1.append(decoder)

    # # Get Bottom Left Bottom and Center
    for decoder in decorderList1:
        if len(decoder) == 6:
            
            decoderSet = set(decoder)

            if containsAll(decoder, numbers[4]):
                four = set(numbers[4])
                markers["Bottom"] = "".join(decoderSet - four - set(markers["Top"]))
                numbers[9] = decoder
                markers["LB"] = "".join(eight - decoderSet)
   
            
            else:
                markers["Center"] = "".join(eight - decoderSet)
                numbers[0] = decoder
        
            
    # Get LT
    chars7 = "".join([x for x in markers.values() if x != ""])
    setChars7 = set(chars7)
    markers["LT"] = "".join(eight - setChars7)
    
    # Filter out the for the fivers
    decoderList2 = [x for x in decorderList1 if len(x) == 5]

    for decode in decoderList2:
        if containsAll(decode, f'{markers["Top"]}{markers["RT"]}{markers["Center"]}{markers["LB"]}{markers["Bottom"]}'):
            numbers[2] = decode
        elif containsAll(decode, f'{markers["Top"]}{markers["RT"]}{markers["Center"]}{markers["RB"]}{markers["Bottom"]}'):
            numbers[3] = decode
        elif containsAll(decode, f'{markers["Top"]}{markers["LT"]}{markers["Center"]}{markers["RB"]}{markers["Bottom"]}'):
            numbers[5] = decode
    return numbers


def counterStr2(daStr):
    daDict = markersCreator(daStr)
    # print(daDict)
    finNumber = ""
    
    newStr = daStr.split("|")
    newStr = "".join(newStr[1]).strip()
    
    numbers = newStr.split(" ")
    for number in numbers:
        for key, value in daDict.items():
            if containsAll(number, value) and len(number) == len(value):
                finNumber = f"{finNumber}{key}"
    #print(finNumber)
    return int(finNumber)
    
def solution1b():
    # daStr = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    # counterStr2(daStr)
    daList = [  "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
            "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
            "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
            "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
            "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
            "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
            "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
            "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
            "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
            "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"]
    
    overallCount = 0
    for item in daList:
        overallCount += counterStr2(item)
    print(overallCount)
    

# solution1b()

def solution2b():
    overallCount = 0
    with open("8.txt") as f:
        report = []
        for line in f:
            cleanLine = line.strip()
            report.append(cleanLine)
    for str in report:
        overallCount += counterStr2(str)
    print(overallCount)

solution2b()