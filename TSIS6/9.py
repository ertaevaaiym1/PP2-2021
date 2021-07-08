def even_nums(n):
    even = []
    for x in n:
        if x % 2 == 0:
            even.append(x)
    return even
print(even_nums([1, 2, 3, 4, 5, 6, 7, 8, 9]))