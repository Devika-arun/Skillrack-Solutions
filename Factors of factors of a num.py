'''
Input: n = 24
Output:
1
1 2
1 3
1 2 4
1 2 3 6
1 2 4 8
1 2 3 4 6 12
1 2 3 4 6 8 12 24
'''
def factors_Of_a_num(n):
    fact = []
    for i in range(1, n+1):
        if n%i == 0:
            fact.append(i)
    return fact

n = 24
factors = []
for i in range(1, n+1):
    if n%i == 0:
        factors.append(factors_Of_a_num(i))
for i in factors:
    print(*i)
