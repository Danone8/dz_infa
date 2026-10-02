size, symb = input().split()

def triang(size, symb):
    for i in range(size):
        n = min(i + 1, size - i)
        print(symb * n)

triang(int(size), symb)
