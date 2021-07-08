def check(a):
    def add(b):
        nonlocal a
        a += 1
        return a+b
    return add
func = check(4)
print(check(4))