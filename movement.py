n = int(input())
multiple = int(n/5)
left = n - multiple*5
if left == 0:
    print(multiple)
else:
    print(multiple+1)