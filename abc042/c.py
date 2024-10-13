N, K = map(int, input().split())
D = list(map(int, input().split()))

def isGood(num):
    while num:
        R = num % 10
        if R in D:
            return False
        num //= 10
    return True

while True:
    if isGood(N):
        print(N)
        exit(0)
    N += 1
