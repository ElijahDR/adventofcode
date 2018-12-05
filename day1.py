def part1():
    freq = 0
    with open("input1.txt") as f:
        for line in f:
            freq += int(line)

    print("day 1, part 1: " + str(freq))

# def part2():
#     # This takes a while, maybe look into faster ways
#     print("THIS WORKS JUST SLOW")
#     freq = 0
#     history = []
#     done = False
#     with open("input.txt") as f:
#         lines = f.readlines()
#     while done == False:
#         for line in lines:
#             freq += int(line)
#             if freq in history:
#                 print(freq)
#                 done = True
#                 break
#             history.append(freq)
#
#             if done == True:
#                 break

# Credit goes to Micah Waring
def part2():
    seen = set()
    with open("input1.txt", "r") as f:
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
