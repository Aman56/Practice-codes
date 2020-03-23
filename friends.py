t = int(input())
for j in range(t):
    n = int(input())
    for i in range(n):
        h = 2 * n - 2*(i+1)
        print('*'*(i+1)+'#'*h+'*'*(i+1))
    print()
