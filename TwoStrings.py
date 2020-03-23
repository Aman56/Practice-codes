from collections import Counter
t = int(input())
for i in range(t):
    s1, s2 = input().split()
    common = Counter(s1) & Counter(s2)
    tot = sum(common.values())
    if (len(s1)+len(s2) - 2*tot) == 0:
        print('YES')
    else:
        print('NO')