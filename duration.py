from datetime import datetime
n = int(input())
for i in range(n):
    sh, sm, eh, em = input().split()
    start = sh+'::'+sm
    end = eh+'::'+em
    start_time = datetime.strptime(start, '%H::%M')
    end_time = datetime.strptime(end, '%H::%M')
    diff = end_time - start_time
    print(diff.seconds // 3600, diff.seconds // 60 % 60)
