#https://www.hackerrank.com/challenges/cut-the-sticks/problem

def cutTheSticks(arr):

    sticks_cut = []

    while(len(arr) != 0):
        sticks_cut.append(len(arr))
        lenght_cut = min(arr)

        arr = list(map(lambda x: x - lenght_cut, arr))
        arr = [x for x in arr if x != 0]

    return(sticks_cut)

#inputs
n = int(input())

arr = list(map(int, input().rstrip().split()))

result = cutTheSticks(arr)

print(result)
