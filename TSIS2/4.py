сlass Solution(object):
    def largestAltitude(self, gain):
        sum = 0
        att = [0]
        gain = input().split()
        for i in range(len(gain)):
        gain[i] = int(gain[i])
        for i in range(len(gain)):
        sum = sum + gain[i]
        att.append(sum)
        if max(att) < 0:
            print(0)
        else:
            print(max(att))