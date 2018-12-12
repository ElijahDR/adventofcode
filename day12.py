def main():
    with open("input/input12.txt") as f:
        lines = [line.rstrip() for line in f]

    lines.remove("")
    initial = lines[0][15:]
    initial = list(initial)
    print("".join(initial))
    oldState = list(initial)
    print(oldState)
    for i in range(5):
        oldState.insert(0, ".")
        oldState.insert(len(oldState), ".")

    print(oldState)
    newState = ["." for i in range(400)]
    notes = lines[1:len(lines)]
    print(notes)

    noteDic = {}
    for note in notes:
        noteDic[note[:5]] = note[-1:]

    # print(noteDic)
    # print(oldState)
    history = []
    for k in range(194):
        if "".join(oldState) in history:
            print("".join(oldState))
            print(k)
        history.append("".join(oldState))
        for i in range(2, len(newState)):
            lookup = oldState[i-2:i+3]
            if len("".join(lookup)) < 5:
                break
            # print("lookup:", "".join(lookup))
            for key, val in noteDic.items():
                # print("key:", key)
                if "".join(lookup) == key:
                    # print("ADDED")
                    # print(newState)
                    # print("val", val)
                    newState[i] = val
                    break


        oldState = list(newState)
        newState = ["." for i in range(400)]

    left = 50000000000 - 194

    total = 0
    x = -5
    for item in oldState:
        if item == "#":
            total += x + left

        x+=1

    print(total)

if __name__ == "__main__":
    main()
