arrSize = 1000000
def createArray(x, y, z= 0 ):
    arr = []
    for i in range(x):
        arr2 = []
        for j in range(y):
            arr2.append(z)
        arr.append(arr2)

    return arr

def cleanLine(line):
    line = line.replace("position", "").replace("velocity", "").replace("=", "").replace("<","").replace(">", "").replace(",", "")
    return line

def getExtremes(data):
    extremes = [arrSize ** 2, arrSize ** 2, 0, 0, 0, 0]
    extremes[0] = min(p[0] for p in data)
    extremes[1] = min(p[1] for p in data)
    extremes[2] = max(p[0] for p in data)
    extremes[3] = max(p[1] for p in data)

    extremes[4] = extremes[2] - extremes[0]
    extremes[5] = extremes[3] - extremes[1]

    return extremes

def show(draw, extremes):
    arr = createArray(extremes[5] + 1, extremes[4] + 1, ".")
    for item in draw:
        arrX = int(item[0] - extremes[2] + extremes[4])
        arrY = int(item[1] - extremes[3] + extremes[5])
        arr[arrY][arrX] = "#"

    for line in arr:
        print("".join(line))


def run(one = True, two = True, inputData = "input/input10.txt"):
    with open(inputData) as f:
        lines = f.readlines()

    data = []
    for line in lines:
        line = cleanLine(line)
        lineArr = line.split()
        lineData = list(map(int, lineArr))
        data.append(lineData)

    done = False
    second = 8000
    best = []
    bestRanges = arrSize
    bestSecond = 0
    bestDraw = []
    bestExtremes = []
    while done == False:
        extremes = [arrSize, arrSize, 0, 0, 0, 0]
        draw = []
        for item in data:
            drawX = int(item[0] + (arrSize / 2) + (second * item[2]))
            drawY = int(item[1] + (arrSize / 2) + (second * item[3]))
            draw.append([drawX, drawY])
            if drawX < extremes[0]:
                extremes[0] = drawX
            if drawY < extremes[1]:
                extremes[1] = drawY
            if drawX > extremes[2]:
                extremes[2] = drawX
            if drawY > extremes[3]:
                extremes[3] = drawY

        extremes[4] = extremes[2] - extremes[0]
        extremes[5] = extremes[3] - extremes[1]

        avg = (extremes[4] + extremes[5]) / 2

        if avg < bestRanges:
            bestDraw = draw
            bestExtremes = extremes
            bestRanges = avg
            bestSecond = second

        second += 1
        if second == 15000:
            done = True
            continue

    if one == True:
        print("day 10, part 1 (required reading):")
        show(bestDraw, bestExtremes)
    if two == True:
        print("day 10, part 2:", bestSecond)

def main(inputData = "input/input10.txt"):
    run(True, True, inputData)

def part1(inputData = "input/input10.txt"):
    main(True, False, inputData)

def part2(inputData = "input/input10.txt"):
    main(False, True, inputData)

if __name__ == "__main__":
    main()
