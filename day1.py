def part1(inputData = "input/input1.txt"):
    freq = 0
    with open(inputData) as f:
        for line in f:
            freq += int(line)

    print("day 1, part 1: " + str(freq))

# Credit goes to Micah Waring
def part2(inputData = "input/input1.txt"):
    seen = set()
    with open(inputData, "r") as f:
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

def main(inputData = "input/input1.txt"):
    part1(inputData)
    part2(inputData)

if __name__ == "__main__":
    main()
