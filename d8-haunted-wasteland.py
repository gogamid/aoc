L = 0
R = 1
START = "AAA"
END = "ZZZ"
if __name__ == "__main__":
    # read from input
    f = open("8.txt", "r")

    # save navigation ex. LLRRLLR
    nav = f.readline().strip()
    # get rid of empty line
    f.readline()

    # save node definitions
    line = " "
    nodes = {}
    curr = START
    while line:
        line = f.readline().strip()
        key = line[:3]
        left = line[7:10]
        right = line[12:15]
        nodes[key] = [left, right]

    # count steps
    step = 0
    i = 0
    while curr != END:
        if nav[i] == "L":
            curr = nodes[curr][L]
        else:
            curr = nodes[curr][R]
        if i + 1 > len(nav) - 1:
            i = 0
        else:
            i = i + 1
        step += 1
    print(step)
