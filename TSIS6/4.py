def reverse(string):
    rstring = ''
    index = len(string)
    while index > 0:
        rstring += string[index - 1]
        index = index - 1
    return rstring
print(reverse(input()))