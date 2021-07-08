def find_max_num_of_two(x, y, z):
    if x > y:
        return x
    return y
def find_max_num_of_three(x, y, z):
    return find_max_num_of_two(x, find_max_num_of_two(y, z))
print(find_max_num_of_three())
