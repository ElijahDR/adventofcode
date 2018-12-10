def cleanLine(line):
    newLine = []
    lineArr = line.split()
    ID = int(lineArr[0].replace("#", ""))

    left = int(lineArr[2].split(",")[0])
    right = int(lineArr[2].split(",")[1].replace(":", ""))
    newLine.append(left)
    newLine.append(right)


    width = int(lineArr[3].split("x")[0])
    height = int(lineArr[3].split("x")[1])
    newLine.append(width)
    newLine.append(height)

    newLine.append(ID)

    return newLine

def makeArr(x, y):
    arr = []
    for i in range(0, x):
        secondArr = []
        for j in range(0, y):
            secondArr.append(0)
        arr.append(secondArr)

    return arr

def part1(inputData = "input/input3.txt"):
    arr = makeArr(1000, 1000)

    lines = 0
    with open(inputData) as f:
        lines = f.readlines()

    for line in lines:
        line = cleanLine(line)
        for i in range(line[0], line[0] + line[2]):
            for j in range(line[1], line[1] + line[3]):
                arr[i][j] += 1

    count = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            if arr[i][j] > 1:
                count += 1

    print("day 3, part 1: " + str(count))
    return arr

def part2(inputData = "input/input3.txt", arr = 0):
    with open(inputData) as f:
        lines = f.readlines()

    if arr == 0:
        arr = makeArr(1000, 1000)
        for line in lines:
            line = cleanLine(line)
            for i in range(line[0], line[0] + line[2]):
                for j in range(line[1], line[1] + line[3]):
                    arr[i][j] += 1

    for line in lines:
        line = cleanLine(line)
        okay = True
        for i in range(line[0], line[0] + line[2]):
            for j in range(line[1], line[1] + line[3]):
                if arr[i][j] > 1:
                    okay = False

        if okay == True:
            print("day 3, part 2: " + str(line[4]))

def main(inputData = "input/input3.txt"):
    arr = part1(inputData)
    part2(inputData, arr)

if __name__ == "__main__":
    main()
