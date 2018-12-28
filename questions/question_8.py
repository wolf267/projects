def rep(str='Hello WORLD!'):
    res = ''
    vowel = 'aeiou'
    for i in str:
        if i in vowel:
            if i.isupper():
                i = 'Iron Yard'
            else:
                i = 'Yard'
            res += i
        else:
            if i.isupper():
                i = 'Iron'
            res += i
    return res

if __name__ == '_main__':
    print(rep(str))
    print('Press to countine...')
