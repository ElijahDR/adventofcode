import time

alphabet = list("qwertyuiopasdfghjklzxcvbnm".upper())
# alphabet = list("abcdef".upper())


def cleanLine(line):
    line = line.split()
    newLine = [line[1], line[7]]
    return newLine

def createArr(x, y):
    arr = []
    for i in range(x):
        arr2 = []
        for j in range(y):
            arr2.append(0)

        arr.append(arr2)

    return arr

def currentlyPossible(req, done):
    possible = []
    for item, needed in req.items():
        if len(done) == 0:
            if needed == done:
                possible.append(item)
        else:
            okay = True
            for thing in needed:
                if thing not in done or item in done:
                    okay = False

            if okay == True:
                possible.append(item)


    for item, needed in req.items():
        if item in done:
            possible = list(filter((item).__ne__, possible))

    return possible



def main():
    # alphabet = list("abcdef".upper())
    with open("input7.txt") as f:
        lines = f.readlines()

    requirements = {}
    for i in range(len(alphabet)):
        requirements[alphabet[i]] = []

    for line in lines:
        line = cleanLine(line)
        requirements[line[1]].append(line[0])
        requirements[line[1]].sort()


    sorted_by_value = sorted(requirements.items(), key=lambda kv: kv[1])
    order = []
    orderSorted = []
    done = False
    current = 0
    while done == False:
        possible = []
        for item, needed in requirements.items():
            if len(orderSorted) == 0:
                if needed == orderSorted:
                    possible.append(item)
            else:
                okay = True
                for thing in needed:
                    if thing not in order or item in order:
                        okay = False

                if okay == True:
                    possible.append(item)

        newPos = [0, 1]
        bestLength = 100
        for item in possible:
            if item in order:
                possible = list(filter((item).__ne__, possible))
                continue
            else:
                if len(requirements[item]) == bestLength:
                    newPos[1] = item
                if len(requirements[item]) < bestLength:
                    newPos = [0, 1]
                    newPos[0] = item

        possible.sort()
        order.append(possible[0])

        orderSorted = sorted(order)
        if len(order) == len(alphabet):
            done = True
            break

    print("".join(order))

    # workers =  [0, 0, 0, 0, 0]
    startTime = time.time()
    workers = [0, 0, 0, 0, 0]
    done = []
    doing = []
    times = [0, 0, 0, 0, 0]
    finished = False
    total = 0

    while finished == False:
        possible = currentlyPossible(requirements, done)
        if len(possible) == 0:
            finished = True
            continue
        for pos in possible:
            i = 0
            for worker in workers:
                if worker == 0 and pos not in workers:
                    workers[i] = pos
                    doing.append(pos)
                    times[i] = (ord(pos) - 64) + 60

                i+=1


        total += 1
        for i in range(len(times)):
            if times[i] > 0:
                times[i] -= 1
            if times[i] == 0:
                done.append(str(workers[i]))
                workers[i] = 0

    print(total)




if __name__ == "__main__":
    import time
    main()
