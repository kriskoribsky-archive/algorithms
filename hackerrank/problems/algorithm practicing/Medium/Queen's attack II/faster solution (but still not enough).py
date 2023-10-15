def queensAttack(n, k, rq, cq, obstacles):
    
    print(("size of chess board: {0} \nnumber of obstacles: {1} \nqueen position: [{2}, {3}] \nobstacles: {4}").format(n, k, rq, cq, obstacles))

    legal_moves = 0

    #rows
    y = cq + 1
    while y != n+1 and [rq, y] not in obstacles:
        y += 1
        legal_moves += 1

    y = cq - 1
    while y != 0 and [rq, y] not in obstacles:
        y -= 1
        legal_moves += 1

    #columns
    x = rq + 1
    while x != n+1 and [x, cq] not in obstacles:
        x += 1
        legal_moves += 1

    x = rq - 1
    while x != 0 and [x, cq] not in obstacles:
        x -= 1
        legal_moves += 1

    #first diagonal (bottom left to top right)
    x = rq + 1
    y = cq + 1
    while x != n+1 and y != n+1 and [x, y] not in obstacles:
        x += 1
        y += 1
        legal_moves += 1


    x = rq - 1
    y = cq - 1
    while x != 0 and y != 0 and [x, y] not in obstacles:
        x -= 1
        y -= 1
        legal_moves += 1

    #second diagonal (top left to bottom right)
    x = rq + 1
    y = cq - 1
    while x != n+1 and y != 0 and [x, y] not in obstacles:
        x += 1
        y -= 1
        legal_moves += 1

    x = rq - 1
    y = cq + 1
    while x != 0 and y != n+1 and [x, y] not in obstacles:
        x -= 1
        y += 1
        legal_moves += 1

    return legal_moves

nk = input().split()
n = int(nk[0])
k = int(nk[1])

rqcq = input().split()
rq = int(rqcq[0])
cq = int(rqcq[1])

obstacles = []
for _ in range(k):
    obstacles.append(list(map(int, input().rstrip().split())))

result = queensAttack(n, k, rq, cq, obstacles)
print("Number of legal moves:", result)
