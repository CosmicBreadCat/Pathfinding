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


def genPathing(start):
    pathing = {}
    existingNeighbours = []



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


print(genPathing(cur_point))
