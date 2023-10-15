def queensAttack(n, k, rq, cq, obstacles):
    
    print(("size of chess board: {0} \nnumber of obstacles: {1} \nqueen position: [{2}, {3}] \nobstacles: {4}").format(n, k, rq, cq, obstacles))

    #calculate default number of moves (rows, columns, diagonals)
    right = n - cq
    left = cq - 1
    up = n - rq
    down = rq - 1

    up_right = min(right, up)
    down_left = min(left, down)
    up_left = min(left, up)
    down_right = min(right, down)

    
    for i in obstacles:
        x = i[0]
        y = i[1]

        #row
        if x == rq:
            if y > cq:
                right = min(right, y - cq - 1)
            else:
                left = min(left, cq - y - 1)
                
        #column
        elif y == cq:
            if x > rq:
                up = min(up, x - rq - 1)
            else:
                down = min(down, rq - x -1)
                
        #diagonal     
        elif abs(x - rq) == abs(y - cq):
            if x > rq:
                if y > cq:
                    up_right = min(up_right, y - cq - 1)
                else:
                    up_left = min(up_left, cq - y - 1)
            else:
                if y > cq:
                    down_right = min(down_right, y - cq - 1)
                else:
                    down_left = min(down_left, cq - y - 1)

      
    legal_moves = right + left + up + down + up_right + down_left + up_left + down_right

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
