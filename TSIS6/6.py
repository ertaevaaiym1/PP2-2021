def string(s):
    a = {'upper_case':0, 'lower_case': 0}
    for x in s:
        if x.isupper():
            a['upper_case'] += 1
        elif x.islower():
            a['lower_case'] += 1
        else:
            pass
    print('string: ', s)
    print('num of upper characters: ', a['upper_case'])
    print('num of lower characters: ', a['lower_case'])
string(input())