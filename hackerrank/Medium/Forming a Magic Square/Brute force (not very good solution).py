def formingMagicSquare(s):
    
    """BRUTE FORCE METHOD (NOT VERY EFFICIENT)"""
    
    #list var for conversion costs
    costs = []
    
    #all 8 possible magic squares with magic constant 15
    magic_squares = [   [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
                        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
                        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
                        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
                        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
                        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
                        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
                        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]
                         
    #compare each magic_square with input square (s) and return minimal cost
    for x in magic_squares:

        cost = 0
            
        for y in range(3):
            for z in range(3):
                cost += abs(x[y][z] - s[y][z])

        costs.append(cost)

    print(costs)
    return min(costs)

s = []

for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))

result = formingMagicSquare(s)

print("result:", result)
