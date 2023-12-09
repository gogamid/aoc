import math

L = 0
R = 1


def get_next(curr, dir):
    if dir == "L":
        return nodes[curr][L]
    else:
        return nodes[curr][R]


def steps_to_ZZZ(start, end):
    step = 0
    i = 0
    curr = start
    while curr != end:
        curr = get_next(curr, nav[i])
        if i + 1 > len(nav) - 1:
            i = 0
        else:
            i = i + 1
        step += 1
    return step


def steps_to_nodes_end_Z():
    keys_A = list(filter(lambda x: x[-1] == "A", list(nodes.keys())))
    print(keys_A)
    n = len(nav)
    steps = []
    for key in keys_A:
        i = 0
        step = 0
        while key[-1] != "Z":
            key = get_next(key, nav[i])
            if i + 1 > n - 1:
                i = 0
            else:
                i += 1
            step += 1
        steps.append(step)

    return math.lcm(*steps)


if __name__ == "__main__":
    # read from input
    f = open("8.txt", "r")

    # save navigation ex. LLRRLLR
    nav = f.readline().strip()
    # get rid of empty line
    f.readline()

    # save node definitions
    line = " "
    nodes: dict[str, list[str]] = {}
    while line:
        line = f.readline().strip()
        if not line:
            break
        key = line[:3]
        left = line[7:10]
        right = line[12:15]
        nodes[key] = [left, right]

    # A) how many steps to reach ZZZ
    steps = steps_to_ZZZ("AAA", "ZZZ")
    print(steps)

    # B) how many steps to reach all nodes ending with Z
    steps = steps_to_nodes_end_Z()
    print(steps)
