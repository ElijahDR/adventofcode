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

def part1():
    arr = []
    for i in range(0, 1000):
        secondArr = []
        for j in range(0, 1000):
            secondArr.append(0)
        arr.append(secondArr)

    lines = 0
    with open("input3.txt") as f:
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

def part2(arr):
    with open("input3.txt") as f:
        lines = f.readlines()

    for line in lines:
        line = cleanLine(line)
        okay = True
        for i in range(line[0], line[0] + line[2]):
            for j in range(line[1], line[1] + line[3]):
                if arr[i][j] > 1:
                    okay = False

        if okay == True:
            print("day 3, part 2: " + str(line[4]))

def main():
    arr = part1()
    part2(arr)



if __name__ == "__main__":
    main()
