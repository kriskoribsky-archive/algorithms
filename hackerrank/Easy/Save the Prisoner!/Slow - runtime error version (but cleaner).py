nms = input().split()

n = int(nms[0])
m = int(nms[1])
s = int(nms[2])

def SaveThePrisoner(n, m, s):
    print("Number of prisoners (n):", n)
    print("Number of sweets (m):", m)
    print("Starting seat (s):", s)

    prisoners = [x for x in range(1, n+1)]

    start = prisoners.index(s)

    print("default prisoners list:", prisoners)
    print("starting index:", start)


    prisoners = prisoners[start:] + prisoners[:start]

    print("sorted prisoners list:", prisoners)

    if n < m:
        last_candy = m-int(m/n)*n

    else:
        last_candy = m


    return prisoners[last_candy-1]


solve = SaveThePrisoner(n, m, s)

print(solve)

    
    
