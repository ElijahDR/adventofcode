class Marble:
    def __init__(self, val):
        self.val = val
        self.next = self
        self.previous = self

    def play(self, marble):
        if marble.val % 23 != 0:
            one = self.next
            two = self.next.next
            marble.next = two
            marble.previous = one
            one.next = marble
            two.previous = marble
            return marble, 0
        else:
            current = self
            for i in range(0, 7):
                current = current.previous

            current.next.previous = current.previous
            current.previous.next = current.next

            return current.next, current.val + marble.val

def createArr(x, y = 0):
    arr = []
    for i in range(x):
        arr.append(0)

    return arr

def part1(inputData = "input.input9.txt"):
    with open(inputData) as f:
        data = f.read().split()

    playersN = int(data[0])
    last = int(data[6])

    marble = Marble(0)
    players = createArr(playersN)
    current = 0
    for i in range(1, last):
        marble, score = marble.play(Marble(i))
        players[current] += score
        current += 1
        if current == playersN:
            current = 0

        if marble.val == last:
            break

    print("day 9, part 1:", max(players))

def part2(inputData = "input/input9.txt"):
    with open(inputData) as f:
        data = f.read().split()

    playersN = int(data[0])
    last = int(data[6]) * 100

    marble = Marble(0)
    players = createArr(playersN)
    current = 0
    for i in range(1, last):
        marble, score = marble.play(Marble(i))
        players[current] += score
        current += 1
        if current == playersN:
            current = 0

        if marble.val == last:
            break

    print("day 9, part 2:", max(players))

def main(inputData = "input/input9.txt"):
    part1(inputData)
    part2(inputData)



if __name__ == "__main__":
    main()
