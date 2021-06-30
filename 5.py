class Solution(object):
    def subtractProductAndSum(self, n):
    n = input('n = ')
    p, sum = 1, 0
    for i in range(len(n)):
    p = p * int(n[i])
    sum = sum + int(n[i])
    print(p - sum)
        