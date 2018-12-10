import time

CHARS = list("abcdefghijklmnopqrstuvwxyz")

def react(data):
    done = False
    oldPoly = data
    while done == False:
        for char in CHARS:
            data = data.replace(char + char.upper(), "").replace(char.upper() + char, "")
        # If no change, return
        if oldPoly == data:
            done = True
            break
        oldPoly = data

    return data

def part1(inputData = "input/input5.txt"):
    with open(inputData) as f:
        data = f.read()

    data = data.rstrip()
    data = react(data)
    print("day 5, part 1: " + str(len(data)))
    return data

def part2(inputData = "input/input5.txt", data = 0):
    if data == 0:
        with open(inputData) as f:
            data = f.read()
        data = data.rstrip()
        data = react(data)

    original = str(data)
    bestLength = len(data)
    bestChar = 0
    for char in CHARS:
        data = data.replace(char, "").replace(char.upper(), "")
        data = react(data)
        length = len(data)
        if length < bestLength:
            bestLength = length
            bestChar = char
        data = str(original)

    print("day 5, part 2: " + str(bestLength))

def main(inputData = "input/input5.txt"):
    dataArr = part1(inputData)
    part2(inputData, dataArr)

if __name__ == "__main__":
    main()
