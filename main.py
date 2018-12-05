import day1, day2, day3, day4, day5
import time

if __name__ == "__main__":
    startTime = time.time()
    day1.main()
    day2.main()
    day3.main()
    day4.main()
    day5.main()
    print("Running took %s seconds" % (time.time() - startTime))
