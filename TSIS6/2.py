def find_sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(find_sum((8, 2, 3, 0, 7)))