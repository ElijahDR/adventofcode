def main(inputData = "input/input8.txt"):
    with open(inputData) as f:
        data = f.read()
        data = data.split()

    data = list(map(int, data))

    # data, metadata = solve(data)
    # metadata = data + metadata
    _, answer = solve1(data)
    print("day 8, part 1:", answer)
    _, answer = solve2(data)
    print("day 8, part 2:", answer)

def part1(inputData = "input/input8.txt"):
    with open(inputData) as f:
        data = f.read()
        data = data.split()

    data = list(map(int, data))
    _, answer = solve1(data)
    print("day 8, part 1:", answer)

def part2(inputData = "input/input8.txt"):
    with open(inputData) as f:
        data = f.read()
        data = data.split()

    data = list(map(int, data))
    _, answer = solve2(data)
    print("day 8, part 2:", answer)

def solve1(data, current = 0):
    childrenN = data[current]
    metas = data[current + 1]
    scores = []

    current += 2
    children = []

    for i in range(0, childrenN):
        current, child = solve1(data, current)
        children.append(child)

    main = sum(data[current:current + metas])
    return current + metas, main + sum(children)

def solve2(data, current = 0):
    value = 0
    childrenN = data[current]
    metas = data[current + 1]

    current += 2
    childrenValues = []

    if childrenN != 0:
        for i in range(childrenN):
            current, childValue = solve2(data, current)
            childrenValues.append(childValue)

        for meta in data[current: current + metas]:
            if meta - 1 < len(childrenValues):
                value += childrenValues[meta - 1]
    else:
        value = sum(data[current: current + metas])

    return current + metas, value

if __name__ == "__main__":
    main()
