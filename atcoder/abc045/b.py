Sa = list(input()); Sa = Sa[::-1]
Sb = list(input()); Sb = Sb[::-1]
Sc = list(input()); Sc = Sc[::-1]

ch = 'a'

while True:
    if ch == 'a':
        if not Sa:
            print('A')
            exit(0)
        ch = Sa.pop()
    elif ch == 'b':
        if not Sb:
            print('B')
            exit(0)
        ch = Sb.pop()
    else:
        if not Sc:
            print('C')
            exit(0)
        ch = Sc.pop()
