N = int(input())
A = list(map(int, input().split()))
S = sum(A)

X1, X2 = S//N, (S//N) + 1

cost = 1e9
for x in [X1, X2]:
    ccost = 0
    for a in A:
        ccost += (x - a) ** 2
    cost = min(cost, ccost)

print(cost)
