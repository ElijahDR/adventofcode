def part1():
    twos = 0
    threes = 0
    with open("input2.txt") as f:
        for line in f:
            added2 = False
            added3 = False
            line = line.strip()
            arr = list(line)
            for item1 in arr:
                count = 0
                for item2 in arr:
                    if item1 == item2:
                        count += 1
                if count == 2 and added2 == False:
                    added2 = True
                    twos += 1
                if count == 3 and added3 == False:
                    added3 = True
                    threes += 1
    print("day 2, part 1: " + str(twos * threes))



def part2():
    with open("input2.txt") as f:
        lines = f.readlines()
        best = 0
        bestX = 0
        bestY = 0
        x = 0
        for line in lines:
            y = 0
            line = line.strip()
            arr = list(line)
            for line2 in lines:
                if y == x:
                    y +=1
                    continue
                line2 = line2.strip()
                arr2 = list(line2)
                count = 0
                for i in range(0, len(arr)):
                    if arr[i] == arr2[i]:
                        count += 1
                if count > best:
                    bestX = x
                    bestY = y
                    best = count
                y += 1
            x += 1
        word1 = lines[bestX]
        word2 = lines[bestY]
        arr1 = list(word1)
        arr2 = list(word2)
        new = []
        for i in range(0, len(arr1)):
            if arr1[i] == arr2[i]:
                new.append(arr1[i])

        print("day 2, part 2: " + "".join(new).rstrip())

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
