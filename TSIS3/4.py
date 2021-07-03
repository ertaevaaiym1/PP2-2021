a = list(input().split())
for i in a:
    if int(i) != 1:
        a.remove(i)
        a.append(i)
            print(*a)