def part1():
    freq = 0
    with open("input/input1.txt") as f:
        for line in f:
            freq += int(line)

    print("day 1, part 1: " + str(freq))

# Credit goes to Micah Waring
def part2():
    seen = set()
    with open("input/input1.txt", "r") as f:
        data = f.read().split("\n")
    freqs = []
    for i in range(0, len(data)):
        freqs.append(int(data[i]))
    acc = 0
    done = False
    while done == False:
        for f in freqs:
            acc += f
            if not acc in seen:
                seen.add(acc)
            else:
                print("day 1, part 2: " + str(acc))
                done = True
                break


def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
