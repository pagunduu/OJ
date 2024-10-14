from collections import defaultdict
import string

S = input()
pos = defaultdict(lambda: [])

for i, ch in enumerate(S):
    pos[ch].append(i)

for ch in string.ascii_lowercase:
    N = len(pos[ch])
    for i in range(1, N):
        if pos[ch][i] - pos[ch][i-1] <= 2:
            print(pos[ch][i-1]+1, pos[ch][i]+1)
            exit(0)

print(-1, -1)
