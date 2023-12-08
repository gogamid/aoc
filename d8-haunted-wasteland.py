L = 0
R = 1


def steps_to_ZZZ(start, end):
    step = 0
    i = 0
    curr = start
    while curr != end:
        if nav[i] == "L":
            curr = nodes[curr][L]
        else:
            curr = nodes[curr][R]
        if i + 1 > len(nav) - 1:
            i = 0
        else:
            i = i + 1
        step += 1
    return step


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
    while line:
        line = f.readline().strip()
        key = line[:3]
        left = line[7:10]
        right = line[12:15]
        nodes[key] = [left, right]

    # A) how many steps to reach ZZZ
    steps = steps_to_ZZZ("AAA", "ZZZ")
    print(steps)
