class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []


def main():
    planets = {}
    with open('input6.txt') as file:
        for line in file.readlines():
            planetA, planetB = line.strip().split(')')
            if planetA not in planets:
                planets[planetA] = Node(planetA, None)
            if planetB not in planets:
                planets[planetB] = Node(planetB, planets[planetA])

            planets[planetA].children.append(planets[planetB])
            planets[planetB].parent = planets[planetA]

    root = planets['COM']
    print(getWeight(root, 0))

    youPath = getPath(planets['YOU'])
    sanPath = getPath(planets['SAN'])
    # -2 cause we add 'YOU' and 'SAN' to the sets
    print(len(youPath ^ sanPath) - 2)


def getWeight(node, weight):
    if len(node.children) == 0:
        node.weight = weight
        return weight

    weight_ = weight
    for child in node.children:
        weight_ += getWeight(child, weight + 1)
    return weight_


def getPath(node):
    path = set()
    while node is not None:
        path.add(node.name)
        node = node.parent
    return path


if _name_ == '_main_':
    main()
