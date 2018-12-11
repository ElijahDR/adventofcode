import time

def createArr(x, y):
    arr = []
    for i in range(x):
        arr2 = []
        for j in range(y):
            arr2.append(0)
        arr.append(arr2)

    return arr

def getPower(x, y, serial):
    power = x * x * y + 20 * x * y + (x + 10) * serial + 100 * y
    power //= 100
    power %= 10
    power -= 5

    return power

def power_sum(grid, x, y, z = 3):
    return sum(grid[x1][y1] for x1 in range(x, x + z) for y1 in range(y, y+z))

def main():
    with open("input/input11.txt") as f:
        data = f.read()
        lines = f.readlines()

    serial = int(data)
    print(serial)
    arr = createArr(300, 300)
    # print(getPower(101, 153, 71))
    for x in range(300):
        for y in range(300):
            power = getPower(x + 1, y + 1, serial)
            arr[x][y] = power

    bestSum = 0
    bestX = 0
    bestY = 0
    bestSize = 0
    history = 0
    oldX = 0
    oldY = 0
    done = False
    for z in range(10, 200):
        if done == True:
            break
        startTime = time.time()
        for x in range(300 - z):
            for y in range(300 - z):
                sum = power_sum(arr, x, y, z)

                if sum > bestSum:
                    history = 0
                    bestSum = sum
                    bestX = x + 1
                    bestY = y + 1
                    bestSize = z

                history+=1
                if history > 200000:
                    done = True
                    break


    print(bestSum)
    print(bestX)
    print(bestY)
    print(bestSize)

if __name__ == "__main__":
    main()
