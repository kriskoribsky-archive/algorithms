#queen's attack 2 problem

#algorithm
def queensAttack(n, k, rq, cq, obstacles):

    #first convert coordinates to zero-based indexing for easier manipulation
    n -= 1
    rq -= 1
    cq -= 1

    for x in obstacles:
        x[0] -= 1
        x[1] -= 1

    #print out inputs
    print(("size of chess board: {0}\nnumber of obstacles: {1} \n queen location: [{2},{3}] \n obstacles: {4}").format(n+1, k, rq, cq, obstacles))

    #generate chess board of n x n size
    chess_board = []

    for x in range(n+1):
        for y in range(n+1):
            chess_board.append([x, y])

    print("\n\nchess board:", chess_board)

    #find default legal moves for queen (without obstacles)
    legal_moves = []

    for x in range(n+1):
        #row
        legal_moves.append([rq, x])
        #column
        legal_moves.append([x, cq])

    #first diagonal (bottom left to top right)
    x = rq
    y = cq
        
    while x != n and y != n:
        x += 1
        y += 1
        legal_moves.append([x, y])

    x = rq
    y = cq

    while x != 0 and y != 0:
        x -= 1
        y -= 1
        legal_moves.append([x, y])

    #second diagonal (top left to bottom right)
    x = rq
    y = cq

    while x != n and y != 0:
        x += 1
        y -= 1
        legal_moves.append([x, y])

    x = rq
    y = cq

    while x != 0 and y != n:
        x -= 1
        y += 1
        legal_moves.append([x, y])

    #remove queen's coordinates from legal moves
    for _ in range(2):
        legal_moves.remove([rq, cq])

    print("\ndefault legal moves:", legal_moves)

    #remove obstacles not affecting the path of queen
    for x in obstacles:
        if x not in legal_moves:
            obstacles.remove(x)

    print("\nvalid obstacles:", obstacles)

    #find legal moves for queen
    for i in obstacles:

        x = i[0]
        y = i[1]
    
        #row
        if i[0] == rq:
            #right side
            if i[1] > cq:
                for x in range(i[1], n+1):
                    legal_moves.remove([rq, x])
            #left side
            elif i[1] < cq:
                for x in range(0, i[1]+1):
                    legal_moves.remove([rq, x])
        #column
        elif i[1] == cq:
            #top
            if i[0] > rq:
                for x in range(i[0], n+1):
                    legal_moves.remove([x, cq])
            elif i[0] < rq:
                for x in range(0, i[0]+1):
                    legal_moves.remove([x, cq])
                    
        #first diagonal (bottom left to top right)
        #top
        elif x > rq and y > cq:
            legal_moves.remove([x, y])
            while x != n and y != n:
                x += 1
                y += 1
                legal_moves.remove([x, y])

        #bottom
        elif x < rq and y < cq:
            legal_moves.remove([x, y])
            while x != 0 and y != 0:
                x -= 1
                y -= 1
                legal_moves.remove([x, y])
               
        #second diagonal (top left to bottom right)
        #top
        elif x > rq and y < cq:
            legal_moves.remove([x, y])
            while x != n and y != 0:
                x += 1
                y -= 1
                legal_moves.remove([x, y])

        #bottom
        elif x < rq and y > cq:
            legal_moves.remove([x, y])
            while x != 0 and y != n:
                x -= 1
                y += 1
                legal_moves.remove([x, y])
                
    print("\nLegal moves:", legal_moves)
    print("\nNumber of legal moves:", len(legal_moves))
        
    return len(legal_moves)             
                
#inputs
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
print("\nresult:", result)
