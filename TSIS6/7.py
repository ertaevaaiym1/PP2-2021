def unique(l):
    a = []
    for x in l:
        if x not in a:
            a.append(x)
    return a
print(unique(input()))