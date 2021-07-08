def paskalt(n):
    a = [1]
    b = [0]
    for x in range(max(n, 0)):
        print(a)
        a = [l + r for l, r in zip(a + b, b + a)]
    return n >= 1
paskalt(9)