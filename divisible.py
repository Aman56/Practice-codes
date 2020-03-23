import math
N = int(input())
data = [int(x) for x in input().split()]
number = ''
for i in range(N):
    if i < N/2:
        digits = int(math.log10(data[i]))
        first = int(data[i]/pow(10, digits))
        number += str(first)
    else:
        last = data[i] % 10
        number += str(last)
if int(number) % 11 == 0:
    print('OUI')
else:
    print('NON')
