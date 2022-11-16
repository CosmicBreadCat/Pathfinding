n = 5
cur_point = (0, 0)
end_point = (4, 4)


def getNextNeighbours(cell, existing):
    neighbours = []
    x, y = cell

    cases = [-1, 1]

    for case in cases:
        new_x = x + case
        new_y = y + case

        if 0 < new_x < n:
            if (x + 1, y) not in existing:
                neighbours.append((new_x, y))
                existing.append((new_x, y))
        if 0 < new_y < n:
            if (x, y + 1) not in existing:
                neighbours.append((x, new_y))
                existing.append((x, new_y))

    return neighbours


def genPathingWeb(start):
    pathingWeb = {}
    existingNeighbours = []
    queue = []
    visited = 0

    while visited < n*n:
        if len(queue) == 0:
            neighbours = getNextNeighbours(start, existingNeighbours)
            pathingWeb[start] = neighbours
            visited += 1
            for neighbour in neighbours:
                queue.append(neighbour)
                existingNeighbours.append(neighbour)
        else:
            for i in queue:
                neighbours = getNextNeighbours(i, existingNeighbours)
                pathingWeb[i] = neighbours
                visited += 1
                for neighbour in neighbours:
                    queue.append(neighbour)
                    existingNeighbours.append(neighbour)
                queue.remove(i)
    return pathingWeb


def BFS(pathing, startPoint):
    visited = [startPoint]
    queue = [startPoint]

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in pathing[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


for k, v in zip(genPathingWeb(cur_point).keys(), genPathingWeb(cur_point).values()):
    print(k, ":", v)
