def countLetters(s):
    print(s)
    if len(s)==0:
        return 0
    if s[-1]=='a' or s[-1]=='b':
        return 1+ countLetters(s[:-1])
    else:
        return countLetters(s[:-1])


def matches(one, two):
    one=one.lower()
    two = two.lower()
    for x in one:
        if x!=' ' and one.count(x)!=two.count(x):
            return False
    for x in two:
        if x!= ' ' and two.count(x)!=one.count(x):
            return False
    return True

x = 'abcv'
v = 'av cb'

print(matches(x,v))




print(sorted(x))
