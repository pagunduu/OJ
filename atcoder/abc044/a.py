N = int(input())
K = int(input())
X = int(input())
Y = int(input())

ans = min(N, K) * X + (N - min(N, K)) * Y
print(ans)
