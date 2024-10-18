S = input()
N = len(S)

tsum = 0
for i in range(1<<(N-1)):
    expr = ''
    for j in range(N):
        expr += S[j]
        if i & (1<<j):
            expr += '+'
    
    tsum += eval(expr)

print(tsum)
