S = input()
K = []

for k in S:
  if k == 'B':
      if K:
        K.pop()
  else:
    K.append(k)

print(''.join(K))
