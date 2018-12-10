arrSize = 500
def cleanLine(line):
    line = line.rstrip()
    line = line.split(", ")
    for i in range(len(line)):
        line[i] = int(line[i])

    return line

def emptyArr(x, y, z = 0):
    arr = []
    for i in range(x):
        arr2 = []
        for j in range(y):
            arr2.append(z)

        arr.append(arr2)

    return arr

def cleanData(data):
    lines = []
    for line in data:
        line = cleanLine(line)
        lines.append(line)

    return lines

def getExtremes(data):
    extremes = [arrSize ** 2, arrSize ** 2, 0, 0]
    extremes[0] = min(p[0] for p in data)
    extremes[1] = min(p[1] for p in data)
    extremes[2] = max(p[0] for p in data)
    extremes[3] = max(p[1] for p in data)

    return extremes

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def part1(inputData = "input/input6.txt"):
    with open(inputData) as f:
        data = f.readlines()

    extremes = getExtremes(cleanData(data))
    arr = emptyArr(arrSize, arrSize, arrSize ** 2)
    lineArrs = []
    all = []
    z = 0

    bestDists = emptyArr(arrSize, arrSize, arrSize**2)
    for line in data:
        line = cleanLine(line)
        if line[0] < extremes[0]:
            extremes[0] = line[0]
        if line[1] < extremes[1]:
            extremes[1] = line[1]
        if line[0] > extremes[2]:
            extremes[2] = line[0]
        if line[1] > extremes[3]:
            extremes[3] = line[1]
        arr[line[0]][line[1]] = 51 + z
        all.append(z)
        for x in range(extremes[0] - 1, extremes[2] + 1):
            for y in range(extremes[1] - 1, extremes[3] + 1):
                bestDist = arrSize ** 2
                coord = [x, y]
                diff = manhattan_distance(coord, line)
                if diff < bestDists[x][y]:
                    arr[x][y] = z
                    bestDists[x][y] = diff
                elif diff == bestDists[x][y]:
                    arr[x][y] = "."

        z += 1

    notInfinite = list(all)
    for i in range(arrSize):
        if arr[extremes[0]][i] in notInfinite:
            notInfinite.remove(arr[extremes[0]][i])
        if arr[i][extremes[1]] in notInfinite:
            notInfinite.remove(arr[i][extremes[1]])
        if arr[extremes[2]][i] in notInfinite:
            notInfinite.remove(arr[extremes[2]][i])
        if arr[i][extremes[3]] in notInfinite:
            notInfinite.remove(arr[i][extremes[3]])

    bestCount = 0
    bestI = 0
    for i in notInfinite:
        count = 0
        for x in range(0, arrSize):
            for y in range(0, arrSize):
                if arr[x][y] == i:
                    count += 1

        if count > bestCount:
            bestCount = count
            bestI = i

    print("day 6, part 1:", bestCount)

    return extremes

    # print(arr)

def part2(inputData = "input/input6.txt", extremes = 0):
    with open(inputData) as f:
        data = f.readlines()

    lines = cleanData(data)
    if extremes == 0:
        extremes = getExtremes(lines)
    count  = 0
    arr = emptyArr(arrSize, arrSize, arrSize**2)
    for i in range(extremes[0], extremes[2]):
        for j in range(extremes[1], extremes[3]):
            total = 0
            for line in lines:
                total += manhattan_distance([i, j], line)

            if total < 10000:
                count += 1

    print("day 6, part 2:", count)

def main(inputData = "input/input6.txt"):
    extremes = part1(inputData)
    part2(inputData, extremes)

if __name__ == "__main__":
    main()
