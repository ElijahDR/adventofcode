import days
import time

if __name__ == "__main__":
    import sys
    day = 0
    part = 0
    inputData = 0
    for i in range(0, len(sys.argv)):
        if sys.argv[i] == "-d":
            day = int(sys.argv[i + 1])
        if sys.argv[i] == "-p":
            part = int(sys.argv[i + 1])
        if sys.argv[i] == "-i":
            inputData = sys.argv[i + 1]

    startTime = time.time()
    days.run(day, part, inputData)
    print("Running took %s seconds" % (time.time() - startTime))
