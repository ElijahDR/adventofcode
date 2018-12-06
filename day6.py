import time

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

def getExtremes(data):
    extremes = [arrSize ** 2, arrSize ** 2, 0, 0]
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

    return extremes

# Credit goes to the internet
def manhattan_distance(p, q):

    if(len(p) != len(q)):
       print("Be sure that both vectors are the same dimension!")
       return

    return sum([abs(p[i]-q[i]) for i in range(len(p))])

def part1():
    startTime = time.time()
    with open("input6.txt") as f:
        data = f.readlines()

    extremes = [arrSize ** 2, arrSize ** 2, 0, 0]
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
        for x in range(0, arrSize):
            for y in range(0, arrSize):
                bestDist = arrSize ** 2
                coord = []
                coord.append(x)
                coord.append(y)
                diff = manhattan_distance(coord, line)
                if diff < bestDists[x][y]:
                    arr[x][y] = z
                    bestDists[x][y] = diff
                elif diff == bestDists[x][y]:
                    arr[x][y] = "."

        z += 1

    notInfinite = list(all)
    for i in range(arrSize):
        if arr[0][i] in notInfinite:
            notInfinite.remove(arr[0][i])
        if arr[i][0] in notInfinite:
            notInfinite.remove(arr[i][0])
        if arr[arrSize - 1][i] in notInfinite:
            notInfinite.remove(arr[arrSize - 1][i])
        if arr[i][arrSize - 1] in notInfinite:
            notInfinite.remove(arr[i][arrSize - 1])

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

    print("Running took %s seconds" % (time.time() - startTime))
    print("day 6, part 1:", bestCount)

    # print(arr)

def part2(extremes = 0):
    startTime = time.time()
    with open("input6.txt") as f:
        data = f.readlines()

    if extremes == 0:
        extremes = getExtremes(data)
    lines = []
    for line in data:
        line = cleanLine(line)
        lines.append(line)
    count  = 0
    arr = emptyArr(arrSize, arrSize, arrSize**2)
    for i in range(extremes[0], extremes[2]):
        for j in range(extremes[1], extremes[3]):
            total = 0
            for line in lines:
                total += manhattan_distance([i, j], line)

            if total < 10000:
                count += 1

    print("Running took %s seconds" % (time.time() - startTime))
    print("day 6, part 2:", count)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
