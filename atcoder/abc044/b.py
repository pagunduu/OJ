from collections import Counter
import string

W = input()
Wcnt = Counter(W)

for ch in string.ascii_lowercase:
    if Wcnt[ch] % 2 == 1:
        print("No")
        exit(0)

print("Yes")
