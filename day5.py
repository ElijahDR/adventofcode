import time

def react(data, chars):
    done = False
    oldPoly = data

    while done == False:
        for char in chars:
            data = data.replace(char + char.upper(), "").replace(char.upper() + char, "")
        if oldPoly == data:
            done = True
            break
        oldPoly = data

    return data

def part1():
    with open("input5.2.txt") as f:
        data = f.read()


    data = data.rstrip()

    chars = []
    for char in data:
        if char.lower() not in chars:
            chars.append(char.lower())

    dataArr = react(data, chars)
    print("day 5, part 1: " + str(len(dataArr)))

def part2():
    with open("input5.txt") as f:
        data = f.read()

    data = data.rstrip()
    dataArr = list(data)

    chars = []
    for char in dataArr:
        if char.lower() not in chars:
            chars.append(char.lower())

    bestLength = len(dataArr)
    bestChar = 0
    for char in chars:
        data2 = data.replace(char, "").replace(char.upper(), "")
        dataArr = react(data2, chars)
        if len(dataArr) < bestLength:
            bestLength = len(dataArr)
            bestChar = char

    print("day 5, part 2: " + str(bestLength))



def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
