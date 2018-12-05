import day1, day2, day3, day4, day5

def run(day = 0, part = 0):
    if (day == 0):
        day1.main()
        day2.main()
        day3.main()
        day4.main()
        day5.main()
    if (day == 1):
        if part == 0:
            day1.main()
        elif part == 1:
            day1.part1()
        elif part == 2:
            day1.part2()
    if (day == 2):
        if part == 0:
            day2.main()
        elif part == 1:
            day2.part1()
        elif part == 2:
            day2.part2()
    if (day == 3):
        if part == 0:
            day3.main()
        elif part == 1:
            day3.part1()
        elif part == 2:
            day3.part2()
    if (day == 4):
        if part == 0:
            day4.main()
        elif part == 1:
            print("Cannot run just part one or two for Day 4, running both...")
            day4.main()
        elif part == 2:
            print("Cannot run just part one or two for Day 4, running both...")
            day4.main()
    if (day == 5):
        if part == 0:
            day5.main()
        elif part == 1:
            day5.part1()
        elif part == 2:
            day5.part2()
