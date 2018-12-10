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


def main():
    with open("input/input10.txt") as f:
        lines = f.readlines()

    arr = createArray(100, 100, ".")
    data = []
    for line in lines:
        line = cleanLine(line)
        lineArr = line.split()
        lineData = list(map(int, lineArr))
        data.append(lineData)




    done = False
    second = 0
    best = []
    bestRanges = arrSize
    bestSecond = 0
    while done == False:
        draw = []
        arr = createArray(arrSize, arrSize, ".")
        for item in data:
            drawX = int(item[0] + (arrSize / 2) + (second * item[2]))
            drawY = int(item[1] + (arrSize / 2) + (second * item[3]))
            arr[drawX][drawY] = "#"
            draw.append([drawX, drawY])

        extremes = getExtremes(draw)
        avg = (extremes[4] + extremes[5]) / 2
        if avg < bestRanges:
            bestRanges = avg
            bestSecond = second


        # for line in arr:
        #     print("".join(line))

        second += 1
        print(second)
        if second == 30:
            done = True
            continue

    print(bestSecond)

if __name__ == "__main__":
    main()
