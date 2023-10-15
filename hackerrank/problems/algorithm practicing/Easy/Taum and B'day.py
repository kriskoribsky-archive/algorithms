#https://www.hackerrank.com/challenges/taum-and-bday/problem

def solve(black, white, black_cost, white_cost, conversion_cost):
    black_paid = 0
    white_paid = 0
    
    if black_cost + conversion_cost < white_cost:
        white_cost = black_cost + conversion_cost
    elif white_cost + conversion_cost < black_cost:
        black_cost = white_cost + conversion_cost
     
    black_paid = black*black_cost
    white_paid = white*white_cost

    return black_paid + white_paid



inputs = input().rstrip().split()


b = int(inputs[0])
w = int(inputs[1])

bc = int(inputs[2])
wc = int(inputs[3])

z = int(inputs[4])


for i in range(t):
    result = solve(b, w, bc, wc, z)
    print(result)
