def palindrome(string):
    left = 0
    right = len(string) - 1
    while right >= left:
        if not string[left] == string[right]:
            return False
        left += 1
        right -= 1
    return True
print(palindrome('banana'))