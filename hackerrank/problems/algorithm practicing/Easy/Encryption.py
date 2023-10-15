#https://www.hackerrank.com/challenges/encryption/problem

import math

def encryption(s):
    print(s)

    row = math.floor(math.sqrt(len(s)))
    column = math.ceil(math.sqrt(len(s)))
    encoded_message = ""
    
    if row * column < len(s):
        row += 1

    grid = []

    for _ in range(row):
        grid.append(s[:column])
        s = s[column:]

    print(grid)

    for _ in range(column):
        for x in range(len(grid)):
            if len(grid[x]) >= 1:
                encoded_message += grid[x][0] 
            grid[x] = grid[x][1:]

        encoded_message += " "

    return encoded_message

s = input()

result = encryption(s)
print(result)
