#Incremental House of Pancakes (Problem A, Google - Code Jam 2020, round 2)

#https://codingcompetitions.withgoogle.com/codejam/round/000000000019ffb9/00000000003384ea
"""
Input
3          -> Number of test cases (1 ≤ T ≤ 1000)
1 2        -> Test case #1 (1 pancakes in left[L] stack and 2 in right[R] stack)
2 2        -> Test case #2
8 11       -> Test case #3

Output
Case #1: 1 1 1      
Case #2: 2 1 0          #x: n, l, r   x -> test case number (starting from 1), n -> customers served, and l and r are the numbers of pancakes that will remain in the left and right stacks
Case #3: 5 0 4
"""


T = int(input(""))
input_list = []

for x in range(T):
    input_list.append(input("").split())

for k in range (len(input_list)):
    print(input_list[k])
    L = int(input_list[k][0])
    R = int(input_list[k][1])
    print(L, R)
    
 






print("\nNumber of test cases:", T)
print("Input list:\n" , input_list)
print("\nOutput:\n")

for b in range(T):
    print("Case #"+str(b+1)+":")



"""
3
1 2
2 2
8 11
"""