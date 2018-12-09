import day1, day2, day3, day4, day5, day6, day7, day8, day9

days = [day1, day2, day3, day4, day5, day6, day7, day8, day9]

def run(day = 0, part = 0):
    if (day == 0):
        for d in days:
            d.main()
    else:
        day = days[day - 1]
        if part == 0:
            day.main()
        if part == 1:
            day.part1()
        if part == 2:
            day.part2()
